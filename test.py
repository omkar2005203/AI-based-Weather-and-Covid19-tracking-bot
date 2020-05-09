#test text sentence to extract entities and intent
#module for integrating RASA in any application 
# function works for only pre-trained model
# # Omkar .R

from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu.model import Metadata, Interpreter
from rasa.nlu import config
from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu.model import Metadata, Interpreter
from rasa.nlu import config
import warnings
warnings.filterwarnings('ignore')


# function  run_nlu(text,Trained_model_folder_location)

def run_nlu(txt,loc): 
	interpreter = Interpreter.load(loc)
	return(interpreter.parse(txt))



#./models/nlu (rasa default path example)
'''
Methodology:

 step 0: install rasa core and nlu,spacy en model with help of pip . select project directory and run command:  rasa init --no-prompt   automatically generates necessary files.
 step 1: train model with RASA trainer GUI  command for that is:  rasa-nlu-trainer  (insure a blank .json training file in same location and train initial model with: rasa train
 step 2: convert .json file to .md with python code as follows:
  (only once after manual training)
 from rasa.nlu.convert import convert_training_data
 convert_training_data(data_file="training_data.json", out_file="data.md", output_format="md", language="")

 step 3: identify intent and entity for your questions : train initial model with command : rasa train
 step 4: In models folder of project trained model will be generated with extension  '.tar.gz ' extract it and go to file nlu.md and copy trained data contents to it as well remove previous contents.
 step 5: re-train model with train command.
 step 6: define your model training path ./models/nlu  and write Action.py file as application.
 step 7: import test module in project test text and get output interms of intent and entities.


'''