from . import *

class Tensorflow_Manager():
    def __init__(self) -> None:
        self._connectedToServer = False
        self._sessionCreated = False
        self.allConfigsDone = False
        self.modelJson = None       # model.to_json()  
        self.optimizerConfig = None # model.optimizer.get_config()
        self.metricsList = None     # model.compiled_metrics._user_metrics
        self.loss = None            # model.compiled_loss._user_losses
        self.lossWeights = None     # model.compiled_loss._user_loss_weights
        self.weightedMetrics = None # model.compiled_metrics._user_weighted_metrics
        
        self.callbackList = None    # Every Element of the List would be the list in itsself where the first index would represent type of Callback Function
                                    # abd rest would represent its configuration params
                                    # Callback Name : type(callback_var).__name__
                                    # Params : callback_var.paramName


    def initiateSessionRequest(self):
        print("\n--------------------------------------------------------------------------------------------------")

        if self.allConfigsDone == False:
            print()
            print("PLEASE CONFIGURE THE MODEL FIRST !!\n")
            print("--------------------------------------------------------------------------------------------------\n")
            return
        
        credentialServer_ipAddress = input("Enter the IP Address of the Server : ")  

        connectedToServer = False

        email , password = None , None

        try:
            requestURL = f"http://{credentialServer_ipAddress}:6666/serverRunning"
            response = requests.get(requestURL)
            if response.status_code == 200:
                data = response.json()
                if data['message'] == "Running":
                    print()
                    print("YOU HAVE CONNECTED TO THE SERVER !!")
                    print()
                    connectedToServer = True

                    # email = input("Enter Your Account Email Address : ")
                    # password = input("Enter Your Account Password : ")
                    # jsMsg = json.dumps({"TYPE" : "CUSTOMERS" , "EMAIL" : email , "PASSWORD" : password})
                    # requestURL = f"http://{credentialServer_ipAddress}:5555/check_node?message={jsMsg}"

                    # try:
                    #     response = requests.get(requestURL)

                    #     if response.status_code == 200:
                    #         if(response.json()['message'] == "VERIFIED"):
                    #             print()
                    #             print("CREDENTIALS VERIFIED !!")
                    #             print()
                    #             credentialsVerified = True
                    #         else:
                    #             print()
                    #             print("INVALID EMAIL OR PASSWORD !!")
                    #             print("--------------------------------------------------------------------------------------------------\n")
                    #             credentialsVerified = False
                    #             return
                    #     else:
                    #         pass
                    # except Exception as error:
                    #     print()
                    #     print(f"THE FOLLOWING ERROR OCCURED WHEN VERIFING THE CREDENTIALS : {error}")
                    #     print("--------------------------------------------------------------------------------------------------\n")
                    #     credentialsVerified = False
                    #     return

                else:
                    print("SERVER IS NOT RUNNING RIGHT NOW !!!")
                    print("--------------------------------------------------------------------------------------------------\n")
                    connectedToServer = False
                    return 
        except requests.exceptions.ConnectionError:
            print()
            print("EITHER SERVER IS NOT RUNNING RIGHT NOW OR THE IP ADDRESS ENTERED IS INCORRECT\nPLEASE CHECK THE ENTERED IP ADDRESS OR ELSE TRY AGAIN LATER")
            print("--------------------------------------------------------------------------------------------------\n")
            connectedToServer = False
            return 
        except Exception as error:
            print()
            print(f"THE FOLLOWING ERROR OCCURED WHEN CONNECTING TO THE SERVER : {error}")
            print("--------------------------------------------------------------------------------------------------\n")
            credentialsVerified = False
            return 

        if(not connectedToServer):
            print()
            print("YOUR ARE NOT CONNECTED TO THE SERVER !!")
            print("PLEASE CONNECT TO THE SERVER FIRST !!")
            print("--------------------------------------------------------------------------------------------------\n")
            return
        
        try:
            email = input("Enter Your Account Email Address : ")
            password = input("Enter Your Account Password : ")
            jsMsg = json.dumps({"TYPE" : "CUSTOMERS" , "EMAIL" : email , "PASSWORD" : password})
            requestURL = f"http://{credentialServer_ipAddress}:6666/requestSessionCreation?message={jsMsg}"
            response = requests.get(requestURL)
            if response.status_code == 200:
                data = response.json()
                if data['message'] == "Request Submitted":
                    print()
                    print("THE REQUEST WAS SUBMITTED SUCCESSFULLY !!")
                    print("INITIALIZE YOU SESSION USING YOUR DESKTOP APPLICATION !!")
                    print()
                    self._sessionCreated = True
                    self._connectedToServer = True
                    print("--------------------------------------------------------------------------------------------------\n")
                    return
                else:
                    print()
                    print(data['message'])
                    print("--------------------------------------------------------------------------------------------------\n")
                    return 
            else:
                print()
                print("SESSION COULD NOT BE CREATED !!")
                print(response.json()['message'])
                print("--------------------------------------------------------------------------------------------------\n")
                return 
        except Exception as error:
            print()
            print(f"THE FOLLOWING ERROR OCCURED WHEN CREATING THE SESSION : {error}")
            print("--------------------------------------------------------------------------------------------------\n")
            return
        


    def validModelLayers(self , layers):
        for layer in [(str(lay.__class__.__module__)).split('.') for lay in layers]:
            if(layer[0] == 'keras'):
                if(layer[1] == 'layers'):
                    pass
                elif(layer[1] == 'engine'):
                    if(layer[2] == 'input_layer'):
                        pass
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def InformationTransfer(self , model):
        self.setModel(model)
        pass

    def setModel(self , model):
        if isinstance(model, keras_models.Sequential) or isinstance(model, keras_models.Model):
            self.modelJson = json.loads(model.to_json())
            if self.validModelLayers(model.layers) == False:
                print("Invalid Model Layers Given !!!")
                self.allConfigsDone = False
                modelJson = None
                return 
            else:
                print("Model Configurations has been Succesfully Noted Down !!")

            if not model.optimizer:
                print("Model has no optimizer")
                print("Please Compile the Model before Sending the Model")
                return
            self.setOptimizer(model.optimizer)
            self.setLoss(model.compiled_loss._user_losses)
            self.setMetrics(model.compiled_metrics._user_metrics)
            self.setLossWeights(model.compiled_loss._user_loss_weights)
            self.setWeightedMetrics(model.compiled_metrics._user_weighted_metrics)
            self.allConfigsDone = True
        else:
            print("Pass a valid model")

    def setOptimizer(self , optimizer):
        if optimizer:
            self.optimizerConfig = optimizer.get_config()
    
    def setLoss(self , loss):
        self.loss = loss
    
    def setMetrics(self , metrics):
        self.metricsList = metrics
    
    def setLossWeights(self , lossWeights):
        self.lossWeights = lossWeights
    
    def setWeightedMetrics(self , weightedMetrics):
        self.weightedMetrics = weightedMetrics

    def printAllConfigs(self):
        print("Model Json : " , self.modelJson)
        print("Optimizer Config : " , self.optimizerConfig)
        print("Loss : " , self.loss)
        print("Metrics : " , self.metricsList)
        print("Loss Weights : " , self.lossWeights)
        print("Weighted Metrics : " , self.weightedMetrics)
    


