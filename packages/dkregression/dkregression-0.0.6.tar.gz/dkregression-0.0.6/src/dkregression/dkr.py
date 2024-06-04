import torch
import nevergrad as ng

class DKR():
    """
    The `DKR` object handles the hyper parameter fitting as well as running the model inference. It ties together the kernel, the observation likelihood and the cross-validation configuration. 
    """
    def __init__(self,kernel,likelihood,cross_validation) -> None:
        """
        Args:
            kernel (Kernel): A kernel object that adheres to the definition of kernels as outlined in the [reference section about kernels](./kernels.md#custom-kernel). 
            likelihood (Likelihood): An observation likelihood object that adheres to the definition of observation likelihoods as outlined in the [reference section about observation likelihoods](./observation_likelihoods.md#custom-observation-likelihoods).
            cross_validation (CrossValidation): In instance of the cross-validation configuration object. The documentation can be found in the approporiate [reference section](./cross_validation.md).
        
        Attributes:
            kernel (Kernel): The kernel object that contains the current estimate of the kernel (hyper) parameters under `kernel.params`.
            likelihood (Likelihood): Likelihood model that is currently used.
            cross_validation (CrossValidation): Cross-validation configuration. The [attributes](./cross_validation.md) can be read, but also overwritten if desired.
            X (torch.Tensor): If set, the input data points of the dataset. The shape is `(n,d_input)`. Is typically set by `DKR.fit` method, but can be overwritten. If not set, has the value `None`.
            Y (torch.Tensor): If set, the output data points of the dataset. The shape is `(n,d_output)`. Is typically set by `DKR.fit` method, but can be overwritten. If not set, has the value `None`.
        """

        self.kernel = kernel
        self.likelihood = likelihood
        self.cross_validation = cross_validation
        self.X = None
        self.Y = None
    
    def _update_kernel_params(self,params):
        assert params.keys() == self.kernel.params.keys()
        assert self.X is not None

        self.kernel.params = params

    def _neg_ll_cross_validation(self):
        assert self.X is not None
        assert self.Y is not None

        dataset = self.cross_validation.split_data(self.X,self.Y)

        log_prob = self.cross_validation.evaluate_likelihood(dataset,self.kernel,self.likelihood)
        return -log_prob.item()

    def _set_kernel_params_and_neg_ll(self,params):
        self._update_kernel_params(params)
        neg_ll = self._neg_ll_cross_validation()

        return neg_ll
    
    def fit(self,X,Y,verbose=0,budget=100):
        """The `DKR.fit` method finds the optimal value for the kernel hyperparameters. 
        Mathematically, the fit method optimizes the average negative log-likelihood over 
        the different cross-validation partitions' held-out data points. The exact 
        configuration of this cross-validation depends on configuration of `DKR.cross_validation`,
        but the goal is to have every data point in the dataset at least once being part of the 
        "test dataset". The optimization backend that is used is Meta's Nevergrad. The optimization
        is bound by `DKR.kernel.params_lower_bound` and `DKR.kernel.params_lower_bound`.

        Args:
            X (torch.Tensor): The "training" input values. Need to be of shape `(n,d_input) even if d_input==1.
            Y (torch.Tensor): The "training" target values. Need to be of shape `(n,d_output) even if d_output==1.
            verbose (int, optional): Defines how verbose the output is. This corresponds to the `verbosity` argument of `nevergrad.optimizers.NGOpt.minimize`.
            budget (int, optional): Defines how many iterations Nevergrad is allowed to run. This maps to the `budget` argument of `nevergrad.optimizers.NGOpt`.
        
        Examples:
            ```py
            import torch   
            from dkregression import DKR
            from dkregression.kernels import RBF
            from dkregression.likelihoods import PoissonLikelihood
            from dkregression.cross_validation import CrossValidation

            X = torch.rand((100,4))  
            Y = torch.randint(0,25,(100,1)) 

            kernel = RBF(X)
            likelihood = PoissonLikelihood()
            cv = CrossValidation()

            # initialization of the DKR model with the kernel, likelihood and cross-validation configuration
            model = DKR(kernel, likelihood, cv)

            # fit the kernel (hyper) parameter(s) in 'verbose' mode with a budget of 200
            model.fit(X,Y,verbose=1,budget=200)
            ```
        """
        self.X = X
        self.Y = Y

        param = ng.p.Dict(**{p:ng.p.Scalar(lower=self.kernel.params_lower_bound[p] ,upper=self.kernel.params_upper_bound[p]) for p in self.kernel.params})
        optimizer = ng.optimizers.NGOpt(parametrization=param, budget=budget)
        recommendation = optimizer.minimize(self._set_kernel_params_and_neg_ll,verbosity=verbose)

        #set optimal kernel parameters
        optimal_kernel_params = {p:recommendation[p].value for p in recommendation}
        self._update_kernel_params(optimal_kernel_params)

    def predict(self,Xq):
        """The `DKR.predict` method returns the parameters of the observation likelihood as defined in `DKR.likelihood.param_names` for each query point in `Xq`. 

        Args:
            Xq (torch.Tensor): Contains all the query points and needs to be of shape `(m,d_input)`

        Returns:
            dict: The keys of this dictionary correspond to `DKR.likelihood.param_names`. Each entry will have a shape of `(m,...)`. This means each entry along the zero-th dimension corresponds to a query point. For example in the case of a Poisson Likelihood, the `DKR.predict` method would return a dictionary with the key "lambda". Stored under the key "lambda" would be a Tensor of shape `(m,1)` where each row contains the estimated rate of the DKR model with a Poisson observation likelihood. 
        
        Examples:
            ```py
            import torch   
            from dkregression import DKR
            from dkregression.kernels import RBF
            from dkregression.likelihoods import PoissonLikelihood
            from dkregression.cross_validation import CrossValidation

            X = torch.rand((100,1))  
            Y = torch.randint(0,25,(100,1)) 

            kernel = RBF(X)
            likelihood = PoissonLikelihood()
            cv = CrossValidation()

            # initialization of the DKR model with the kernel, likelihood and cross-validation configuration
            model = DKR(kernel, likelihood, cv)

            # fit the kernel (hyper) parameter(s)
            model.fit(X,Y)

            # model inference for 50 points equally spaced from 0 to 1
            Xq = torch.linspace(0,1,50).reshape(-1,1)
            Yq = model.predict(Xq)
            ```
        """
        assert self.X is not None
        assert self.Y is not None

        k = self.kernel.kernel_matrix(self.X,Xq)
        likelihood_params = self.likelihood.compute_params(k,self.X,self.Y,self.kernel,eval=True)

        return likelihood_params
