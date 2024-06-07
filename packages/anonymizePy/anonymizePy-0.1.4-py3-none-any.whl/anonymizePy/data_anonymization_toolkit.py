# Data Anonymization Toolkit
# 
# Created by Aussie Frost
# 
# This framework defines methods to remove Personally Identifiable Information (PII) from a csv.
# 
# Updated 6/6/2024

# supress some ugly warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", message="Pandas requires version '1.3.6' or newer of 'bottleneck'")
warnings.filterwarnings("ignore", category=UserWarning, module="spacy.util")

# ### Import dependencies
# import standard libraries
import subprocess
import sys
import os
import glob
import random
import logging

import importlib.resources as pkg_resources


import numpy as np
import pandas as pd
import regex as re
import spacy
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

package_level_resources_path = 'anonymizePy.resources.src'

# ### Install nlp models AUTOMATE THIS PROCESS
# !NOTE -- you must install this model: https://spacy.io/models/en#en_core_web_lg
# - command to install model: python -m spacy download en_core_web_lg
# !NOTE -- you must install this model: https://huggingface.co/beki/en_spacy_pii_distilbert
# - command to install model: pip install https://huggingface.co/beki/en_spacy_pii_distilbert/resolve/main/en_spacy_pii_distilbert-any-py3-none-any.whl

def check_and_install_spacy_model(model_name):
    """Check if a spacy model is installed, and install it if not."""
    try:
        spacy.load(model_name)
    except OSError:
        print(f"Model '{model_name}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "spacy", "download", model_name])
        print(f"Model '{model_name}' installed successfully.")

    print(f"Model '{model_name}' was loaded.")
    return spacy.load(model_name)

# Check and install the 'en_spacy_pii_distilbert' model
nlp1 = check_and_install_spacy_model("en_spacy_pii_distilbert")
usingNLP1 = True

class ResourceManager:
    def __init__(self):
        self.resources = []
        self.ignore_list = []
        self.separator = ','

    def resource_loader(self, resource_package, resource_name, sorted=False):
        """Ensures file exists, then loads the text file into the resources list as a nested list, sorted ascending if preferred."""
        try:
            # Read the file in, then possibly sort it
            with pkg_resources.open_text(resource_package, resource_name) as file:
                mylist = file.read().split(self.separator)
            if sorted:
                mylist = np.sort(mylist)

            # Check special case: if ignore_list, handle accordingly
            if "ignore_list" in resource_name:
                self.ignore_list = mylist
            else:
                self.resources.append(mylist)
        except FileNotFoundError:
            print(resource_name, "is not a valid path. Resource could not be loaded.")

    def load_resources(self, resource_package, paths_list, sorted=False, separator=','):
        """Loads each path as a data resource in self.resources list."""
        if separator != self.separator:
            self.separator = separator

        for path in paths_list:
            self.resource_loader(resource_package, path, sorted=sorted)

    def get_resources(self, ignore_list=False):
        """Get the loaded resources and return them."""
        if ignore_list:
            return self.ignore_list
        return self.resources

    def get_txt_file_paths(self, directory):
        """Get a list of paths to all .txt files in the given directory."""
        if not directory.endswith('/'):
            directory += '/'
        txt_files = glob.glob(os.path.join(directory, '*.txt'))
        return txt_files
    

# import resource files as X_list where X is respective name of list
#resource = ResourceManager()
#lanestreets_list = resource.load_resources(['../resources/lanestreets_list/lanestreets_list.txt'])
#states_list = resource.load_resources(['../resources/states_list/states_list.txt'])

class PIIGenerator:
    def __init__(self):
        self.resource_manager = ResourceManager()

    def generate_random_names(self):

        # define default name resources
        first_names_default = [
            "John", "Jane", "David", "Emily", "Michael", "Sarah", "William", "Jennifer", "Robert", "Mary-Sue"
            "Jessica", "Andrew", "Dr. Ashley", "James", "Amanda", "Sir Matthew", "Christina", "Daniel", "Elizabeth",
            "Joseph", "Nicole", "Anthony", "Margaret", "Kevin", "Laura", "Bryan", "Miss Alexis", "Nicholas", "Katherine",
            "Aiden", "Bella", "Carter", "Delilah", "Ethan", "Fiona", "Grayson", "Hazel", "Isaiah", "Juliet",
            "Kai", "Luna", "Mason", "Nora", "Oliver", "Penelope", "Quentin", "Riley", "Sebastian", "Tessa",
            "Uriah", "Violet", "Winston", "Xena", "Yosef", "Zoe", "Abram", "Beatrice", "Cedric", "Daphne",
            "Eliot", "Freya", "Gideon", "Harriet", "Idris", "Juno", "Knox", "Leia", "Milo", "Naomi",
            "Oscar", "Phoebe", "Reece", "Sienna", "Theo", "Uma", "Victor", "Willow", "Xavier", "Yasmin",
            "Zane", "Adele", "Blaine", "Cora", "Dexter", "Elsie", "Flynn", "Gracie", "Holden", "Iris", "Julia",
            "Jasper", "Keira", "Levi", "Matilda", "Nolan", "Olive", "Paxton", "Quinn", "Rowan", "Scarlett",
            "Tristan", "Ursula", "Vaughn", "Whitney", "Xander", "Yara", "Zack", "Alma", "Barrett", "Celeste",
            "Drake", "Esme", "Finn", "Gemma", "Hugo", "Ivy", "Jonah", "Kyla", "Lionel", "Mira", "Nico",
            "Octavia", "Pierce", "Rosalie", "Soren", "Thalia", "Ulysses", "Verity", "Wesley", "Yvette", "Charlie"
        ]
        last_names_default = [
            "Abbott", "Black", "Chapman", "Duffy", "Ellison", "Finch", "Griffith", "Harlow", "Ingram", "Jennings",
            "Knight", "Lowe", "Maxwell", "Norris", "Osborne", "Pike", "Quinn", "Rhodes", "Sherwood", "Tate",
            "Underwood", "Vance", "Whitfield", "York", "Adler", "Barron", "Connor", "Donahue", "Easton", "Field",
            "Golden", "Hartford", "Ivy", "Joyner", "Kessler", "Lawton", "Merritt", "North", "Overton", "Pritchard",
            "Quick", "Rivers", "Sterling", "Thorne", "Upton", "Vaughn", "Waverly", "Xavier", "Youngblood", "Ziegler",
            "Archer", "Beck", "Colby", "Dalton", "Everett", "Frost", "Garrison", "Hammond", "Irvine", "Justice",
            "Kipling", "Langston", "Morrow", "Noble", "Oakley", "Parson", "Quest", "Reilly", "Sawyer", "Thrasher",
            "Ulrich", "Valentine", "Warner", "Xiong", "Yost", "Zimmermans", "Ashby", "Birch", "Crowley", "Davenport",
            "Emerson", "Forrester", "Gilmore", "Hale", "Irwin", "Jasper", "Kent", "Law", "Meadow", "Northwood",
            "O'Donnell", "Pace", "Quill", "Riddle", "Sloan", "Tanner", "Upshaw", "Vincent", "Welles", "Younger", "Bickford"
        ]

        # Load optional name resources
        self.resource_manager.load_resources(package_level_resources_path, ['firstnames_list.txt', 'lastnames_list.txt'], sorted=True)

        # If first_names was loaded, use it
        first_names = self.resource_manager.get_resources()[0]
        if len(first_names) == 0:
            first_names = first_names_default

        # If last names was loaded, use it
        last_names = self.resource_manager.get_resources()[1]
        if len(last_names) == 0:
            last_names = last_names_default
        
        # create name formats
        name_formats = []
        for _ in range(5):

            # generate random full name
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            
            # append to list
            name_formats.append(name)

        return name_formats

    # run PII insertion methods
    def generate_pii(self, text):
        """Generate a random call transcription based on predefined templates."""

        # check to ensure text is in fact a string
        if not isinstance(text, str):
            return text

        # define faux identifiers to insert
        name_formats = self.generate_random_names()
        date_formats = ["2023-10-26", "12/04/2022", "August 15, 1999", "03.11.2018", "2010-02-02", "January 31", "2 Feb", "June 14", "September 22", "Mar 21st", "Apr 1"]
        location_formats = ["123 Main St, San Francisco, CA 12345", "567 Elm St, Eugene, OR 54321", "42 Park Way", "81915 East 24th Ave, Eugene, OR"
                        "15161 Thornberry Lane, Eugene", "51 West 13th St, Eugene, OR 98412", "2481 Jefferson St"]
        age_formats = ["17", "21", "25", "49", "72"]
        facility_formats = ["5th Street Market", "Thermofisher Dynamics", "Target", "White Bird Clinic"]
        language_formats = ["English", "Spanish", "French", "Chinese", "Japanese", "Korean"]

        # find each anonymized identifier, and replace it with a randomly generated identifying feature
        text = text.replace("(NAME)", random.choice(name_formats))
        text = text.replace("(DATE)", random.choice(date_formats))
        text = text.replace("(AGE)", random.choice(age_formats))
        text = text.replace("(LOCATION)", random.choice(location_formats))
        text = text.replace("(FACILITY NAME)", random.choice(facility_formats))
        text = text.replace("(LANGUAGE)", random.choice(language_formats))

        return text

    def insert_pii(self, in_datapath, out_datapath):
        """ This function takes a csv, parces through each cell and 
        inserts PII whenever a PII-related label is detected.

        Args:s
        in_datapath: path to a labeled dataset
        out_datapath: path to where you would like the faux data
        """
        # read the data in
        data = pd.read_csv(in_datapath)

        print("Data loaded. Creating data with faux PII.")

        text_columns = data.select_dtypes(include=['object']).columns
        for col in text_columns:

            # display column that is being anonymized
            print(f" - Adding identifiers to column: {col}")
            data[col] = data[col].apply(self.generate_pii)

        # output the data to a csv
        data.to_csv(out_datapath, index=False)
        print(" --> Data with faux PII saved to", out_datapath, "\n")

# ## Defining case narrative anonymizer functions
# This section contains a script for anonymizing a case narrative dataset.

class DataAnonymizer:
    def __init__(self, resource_paths=[]):
        self.resource_manager = ResourceManager()
        #self.resource_manager.load_resources(resource_paths)
        self.use_ner = True
        self.use_regex = True
        self.use_resources = True
        self.ignore_columns = []

    # ### Method: RegEx String Replacement
    # This method involves defining regular expression patterns, then deploying these RegEx methods to further anonymize the data.
    def regex_remover(self, text):
        """ Primary function to use RegEx patterns to remove sensitive data from
        case narratives. Note that case is ignored at each call of the re.sub
        function. This function returns a modified string where data has been removed.

        Args:
        text (str): a string of text to be anonymized

        Returns:
        text (list): a modified version of a string (or other unchanged input if not)
        """

        # ensure text is string (and is not null)
        if not isinstance(text, str):
            return text
        
        # define regex patterns
        phone_pattern = r"\(?\b(\d{3})\)?[-.\s]*(\d{3})[-.\s]*(\d{4})\b"
        address_pattern = r"\b\d+\s(?:[A-Za-z0-9]+\s)*(?:St|Street|Rd|Road|Ave|Avenue|Blvd|Boulevard|Pl|Place|Lane|Ln|Drive|Dr|Court|Ct|Terrace|Ter|Way)\b(?:[,.\s]|$)"
        web_pattern = r'(https?:\/\/)?(?:www\.)?[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}(?:\/\S*)?'
        ip_pattern = r"\b((?:\d{1,3}\.){3}\d{1,3}|([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|:([0-9a-fA-F]{1,4}:){1,7}|::(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4})\b"
        zip_pattern = r"\b\d{5,}\b"
        date_pattern = r"\b(?:\d{1,2}(st|nd|rd|th)?\s?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)|\d{1,2}/\d{1,2}/?\d{2,4}|\d{4}-\d{2}-\d{2})\b"
        month_pattern = "\b(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\b"
        #num_pattern = r"\b\w*[\d]+\w*\b"
        prefix_pattern = r"\b(Dr|Dr\.|Mr|Mr\.|Mrs|Mrs\.|Ms|Ms\.|Miss|Miss\.|Sir|Madam)\b"
        
        # apply RegEx pattern for each target feature
        text = re.sub(address_pattern, "(LOCATION)", text, flags=re.IGNORECASE)
        text = re.sub(zip_pattern, "(LOCATION)", text, flags=re.IGNORECASE)
        text = re.sub(date_pattern, "(DATE)", text, flags=re.IGNORECASE)
        text = re.sub(month_pattern, "(DATE)", text, flags=re.IGNORECASE)
        text = re.sub(web_pattern, "(WEBSITE)", text, flags=re.IGNORECASE)
        text = re.sub(ip_pattern, "(IP)", text, flags=re.IGNORECASE)
        text = re.sub(phone_pattern, "(PHONE)", text, flags=re.IGNORECASE)
        #text = re.sub(num_pattern, "(NUMBER)", text, flags=re.IGNORECASE)
        text = re.sub(prefix_pattern, "(PREFIX)", text, flags=re.IGNORECASE)
        
        return text

    # ### Method: Natural Language Processing and Named Entity Recognition with spaCy
    def nlp0_anonymize_text(self, text, nlp):
        """ Primary function to deploy a spaCy NLP model and remove
        target features that are identified in the text.

        Args:
        text (str): a string of text to be anonymized 

        Returns:
        text (str): a modified version of a string (or other unchanged input if not)
        """

        if not isinstance(text, str):
            return text
        
        doc = nlp(text)

        """
        # process the text with the NLP model
        print("Entity labels:")
        for label in nlp.get_pipe("ner").labels:
            print(label)
        """

        # get ignore_list (if it exists)
        ignore_list = self.resource_manager.get_resources(ignore_list=True)
        # make ignore_list lower
        ignore_list = [x.lower() for x in ignore_list]

        # Create a list to store the spans that need to be replaced
        replacements = []

        for ent in doc.ents:
            if ent.text in ignore_list:
                continue
            elif ent.label_ in ["TIME", "DATE"]: 
                replacements.append((ent.start_char, ent.end_char, "(DATE)"))
            elif ent.label_ == "NRP":
                replacements.append((ent.start_char, ent.end_char, "(NRP)"))
            elif ent.label_ == "ORG":
                replacements.append((ent.start_char, ent.end_char, "(ORGANIZATION)"))
            if ent.label_ == "LANGUAGE": 
                replacements.append((ent.start_char, ent.end_char, "(LANGUAGE)"))

        # Replace the text in reverse order of positions to avoid messing up the indices
        for start, end, replacement in sorted(replacements, reverse=True):
            text = text[:start] + replacement + text[end:]

        return text

    def nlp1_anonymize_text(self, text, nlp):
        """ Primary function to deploy a spaCy NLP model and remove
        target features that are identified in the text.

        Args:
        text (str): a string of text to be anonymized 

        Returns:
        text (str): a modified version of a string (or other unchanged input if not)
        """

        if not isinstance(text, str):
            return text
        
        doc = nlp(text)

        """
        # process the text with the NLP model
        print("Entity labels:")
        for label in nlp.get_pipe("ner").labels:
            print(label)
        """

        # get ignore_list (if it exists)
        ignore_list = self.resource_manager.get_resources(ignore_list=True)
        # make ignore_list lower
        ignore_list = [x.lower() for x in ignore_list]

        # Create a list to store the spans that need to be replaced
        replacements = []

        for ent in doc.ents:
            if ent.text.lower() in ignore_list:
                continue
            elif ent.label_ == "DATE_TIME":
                replacements.append((ent.start_char, ent.end_char, "(DATE)"))
            elif ent.label_ == "LOC":
                replacements.append((ent.start_char, ent.end_char, "(LOCATION)"))
            elif ent.label_ == "PER": 
                replacements.append((ent.start_char, ent.end_char, "(NAME)"))

        # Replace the text in reverse order of positions to avoid messing up the indices
        for start, end, replacement in sorted(replacements, reverse=True):
            text = text[:start] + replacement + text[end:]

        return text

    # ### Method: Predefined Term Replacement
    # The first part of this method uses an aggregated set of first names registered at least five times in the SSA database from years 1880 through 2022. We call this method last as it is the most distructive to the original database.
    # Then, this method uses a set of states and their shorthand forms such that states can be caught and replaced.

    def term_remover(self, text, resource_list, replacement_text):
        """ Replaces terms in the given text with replacement_text, 
        handling names case-insensitively.
        
        Args:
        text (str): a string of text to be anonymized 
        resource_list (list): a list of predefined terms that should be removed from the text
        replacement_text (string): a string that will replace any removed data

        Returns:
        text_anonymized (str): a modified version of a string
        """

        # prepare regex pattern for case-insensitive matching
        pattern = r'\b(' + '|'.join(map(re.escape, resource_list)) + r')\b'
        regex = re.compile(pattern, re.IGNORECASE)
        
        # replace occurrences of any names in the text using a regex substitution
        text_anonymized = regex.sub(replacement_text, text)
        
        return text_anonymized

    def get_identifier_and_clean_list(self, list):
        """ Helper function to get a list's identifier and return that
        formatted identifier and the updated list without the identifier.

        Args:
        list (list): a list
        """

        # get replacement term
        replacement_term = list[0]

        # format as an identifier
        identifier = f"({replacement_term})"

        # ignore first term in original list
        list_without_id = list[1:]

        return identifier, list_without_id

    def term_replacement(self, text):
        """ This method allows for using resource lists to find and remove
        specified terms from a string. The terms are specified in the
        resources directory (see resources/README.md for more info).

        Args:
        text (str): string with terms to remove

        Returns:
        text (str): updated string
        """
        
        if not isinstance(text, str):
            return text

        replacement_lists = self.resource_manager.get_resources()
        
        # for each list, remove terms from text that are contained the list
        for list in replacement_lists:

            # get identifier and list without identifier
            identifier, list_without_id = self.get_identifier_and_clean_list(list)

            # pass to term_remover
            text = self.term_remover(text, list_without_id, identifier)
        
        return text

    def anonymize_columns(self, data):
        """ This function anonymizes each text column of a DataFrame by checking their 
        data type. The columns are replaced with their anonymized versions.

        Args:
        data (Pandas DataFrame): a DataFrame that is to be anonymized

        Returns:
        data (Pandas DataFrame): an anonymized DataFrame
        """

        # select columns that include text
        text_columns = data.select_dtypes(include=['object']).columns

        # define columns to ignore
        ignore_columns = self.ignore_columns

        for col in text_columns:
            
            # ignore specified columns
            if col not in ignore_columns:

                # display column that is being anonymized
                print(f" - Anonymizing column: {col}")

                # apply data_anonymizer to column and update column contents
                data[col] = data[col].apply(self.data_anonymizer_model)
        return data
    
    # ## Defining the case anonymization pipeline flow
    def data_anonymizer_model(self, text):
        """ This helper function takes in text, which in this case is a component 
        of a case narrative, and returns an anonymized version of that text, 
        where any identifying information is found and replaced with the name 
        of the feature that it corresponds to.

        Args:
        text (str): a string of text to be anonymized

        Returns:
        text (str): a modified version of a string
        """

        # METHOD-- natural language processing:
        # use NLP to anonomize target features
        if self.use_ner == True:
            text = self.nlp1_anonymize_text(text, nlp1)

        # METHOD-- RegEx replacement:
        if self.use_regex == True:
            text = self.regex_remover(text)
        
        # METHOD-- predefined term replacement:
        if self.use_resources == True:
            text = self.term_replacement(text)
            
        return text

    def anonymizer(self, in_datapath, out_datapath, separator=',', use_ner=True, use_regex=True, use_resources=True, ignore_columns=[]):
        """
        This is the main call to run the anonymizer. It takes an input data path
        and output data path (both defined at the top of the script). The
        input data csv is read into a Pandas DataFrame, and then the
        anonymize_columns method is called on the entire dataset. The
        anonymized dataset is then written to an output csv.

        Args:
        in_datapath (csv or alt. text separated file): dataset to be anonymized
        out_datapath (csv): anonymized dataset is written to this path
        seperator (char) [',' by default, optional]: text separater, a comma as default
        use_ner (bool) [True by default, optional]: decides if Named Entity Recognition will be used
        use_regex (bool) [True by default, optional]: decides if RegEx replacement will be used
        use_resources (bool) [True by default, optional]: decides if predefined term replacement will be used
        ignore_columns (list) [empty by default, optional]: provide a list of columns you would like to ignore

        Output:
        a csv at the path specified by out_datapath
        """

        # save config args
        self.use_ner = use_ner
        self.use_regex = use_regex
        self.use_resources = use_resources
        self.ignore_columns = ignore_columns

        # read input dataset into a csv
        data = pd.read_csv(in_datapath, sep=separator)
        print("Data loaded. Starting anonymization process.")

        # define resources path
        txt_file_paths = self.resource_manager.get_txt_file_paths(package_level_resources_path)

        # load in resources
        self.resource_manager.load_resources(package_level_resources_path, txt_file_paths)

        # run the anonymize script on each column
        anonymized_data = self.anonymize_columns(data)

        # write the anonymized data to an output path
        anonymized_data.to_csv(out_datapath, index=False)
        print(" --> Anonymized data saved to", out_datapath, "\n")

class ModelEvaluator:
    def __init__(self):
        pass

    # ## Evaluating the case anonymization model performance
    def extract_unique_labels(self, data):
        """
        Extract unique labels present in the dataset.

        Args:
        data (Pandas DataFrame): The dataset from which to extract labels

        Returns:
        labels (set): A set of unique labels found in the dataset
        """
        labels = set()
        for col in data.columns:
            unique_values = data[col].unique()
            for value in unique_values:
                if isinstance(value, str):
                    for word in value.split():
                        if word.startswith('(') and word.endswith(')') and word[1:-1].isupper():
                            labels.add(word)
        return labels
    
    def calc_metric_values(self, metrics_dict):
        tp = metrics_dict['tp']
        fp = metrics_dict['fp']
        tn = metrics_dict['tn']
        fn = metrics_dict['fn']
        
        accuracy = (tp + tn) / (tp + fp + tn + fn) if (tp + fp + tn + fn) != 0 else 0
        precision = tp / (tp + fp) if (tp + fp) != 0 else 0
        recall = tp / (tp + fn) if (tp + fn) != 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
        
        return accuracy, precision, recall, f1

    def calculate_metrics(self, true_data, pred_data, labels):
        """
        Calculate the evaluation metrics based on true and predicted data.

        Args:
        true_data (Pandas Series): True labels
        pred_data (Pandas Series): Predicted labels
        labels (set): Set of unique labels

        Returns:
        metrics (dict): Dictionary containing overall and per label metrics
        """
        metrics = {label: {'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0} for label in labels}
        overall_metrics = {'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0}
        
        for true, pred in zip(true_data, pred_data):
            for label in labels:
                true_has_label = label in true
                pred_has_label = label in pred

                if true_has_label and pred_has_label:
                    metrics[label]['tp'] += 1
                    overall_metrics['tp'] += 1
                elif not true_has_label and pred_has_label:
                    metrics[label]['fp'] += 1
                    overall_metrics['fp'] += 1
                elif not true_has_label and not pred_has_label:
                    metrics[label]['tn'] += 1
                    overall_metrics['tn'] += 1
                elif true_has_label and not pred_has_label:
                    metrics[label]['fn'] += 1
                    overall_metrics['fn'] += 1

        overall_results = self.calc_metric_values(overall_metrics)
        label_results = {label: self.calc_metric_values(metrics[label]) for label in labels}
        
        return overall_results, label_results


    def evaluate_model(self, labeled_datapath, unanonymized_datapath, anonymized_datapath, log_filepath='output/anonymization_metrics.log', separator=','):
        """
        This function evaluates the performance of the anonymization model by comparing
        the anonymized data with the labeled and un-anonymized data.

        Args:
        labeled_datapath (csv): path to the labeled dataset
        unanonymized_datapath (csv): path to the un-anonymized dataset
        anonymized_datapath (csv): path to the anonymized dataset
        log_filepath (path) [optional]: path to performance log
        separator (char) [optional]: text separator, a comma as default

        Output:
        Outputs the evaluation metrics in a log file
        """

        # ### Set up output log

        # Ensure the directory for the log file exists
        log_dir = os.path.dirname(log_filepath)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Open the file in write mode to truncate it if it exists
        with open(log_filepath, 'w'):
            pass

        # Configure logging to write to a file
        logging.basicConfig(filename=log_filepath, level=logging.INFO, format='%(message)s')

        # Read the datasets
        labeled_data = pd.read_csv(labeled_datapath, sep=separator)
        unanonymized_data = pd.read_csv(unanonymized_datapath, sep=separator)
        anonymized_data = pd.read_csv(anonymized_datapath, sep=separator)

        print("Data loaded. Evaluating model performance.")
        
        # Ensure the datasets have the same columns
        assert set(labeled_data.columns) == set(unanonymized_data.columns) == set(anonymized_data.columns), "Column mismatch between datasets"
        
        # Extract unique labels from the labeled dataset
        original_labels_set = self.extract_unique_labels(anonymized_data)
        labeled_labels_set = self.extract_unique_labels(labeled_data)
        
        # Merge the unique labels without duplicates
        labels = original_labels_set.union(labeled_labels_set)

        # Remove unneccicary labels
        labels_to_remove = ["(X2)", "(WEAPON)", "(BETTER?)", "(AGE)", "(OCCUPATION)"]
        labels = [term for term in labels if term not in labels_to_remove]
        
        # Calculate and output baseline metrics
        logging.info("Baseline Metrics (Unanonymized vs Labeled):")
        baseline_overall, baseline_labels = self.calculate_metrics(labeled_data.stack(), unanonymized_data.stack(), labels)
        logging.info(f"Overall - Accuracy: {baseline_overall[0]:.4f}, Precision: {baseline_overall[1]:.4f}, Recall: {baseline_overall[2]:.4f}, F1 Score: {baseline_overall[3]:.4f}")
        for label, metrics in baseline_labels.items():
            logging.info(f"{label} - Accuracy: {metrics[0]:.4f}, Precision: {metrics[1]:.4f}, Recall: {metrics[2]:.4f}, F1 Score: {metrics[3]:.4f}")
        logging.info("")

        # Calculate and output anonymization metrics
        logging.info("Anonymization Metrics (Anonymized vs Labeled):")
        anonymization_overall, anonymization_labels = self.calculate_metrics(labeled_data.stack(), anonymized_data.stack(), labels)
        logging.info(f"Overall - Accuracy: {anonymization_overall[0]:.4f}, Precision: {anonymization_overall[1]:.4f}, Recall: {anonymization_overall[2]:.4f}, F1 Score: {anonymization_overall[3]:.4f}")
        for label, metrics in anonymization_labels.items():
            logging.info(f"{label} - Accuracy: {metrics[0]:.4f}, Precision: {metrics[1]:.4f}, Recall: {metrics[2]:.4f}, F1 Score: {metrics[3]:.4f}")
        logging.info("")

        # Calculate and output metric differences
        logging.info("Metric Differences (Anonymized vs Baseline):")
        for label in labels:
            accuracy_diff = anonymization_labels[label][0] - baseline_labels[label][0]
            precision_diff = anonymization_labels[label][1] - baseline_labels[label][1]
            recall_diff = anonymization_labels[label][2] - baseline_labels[label][2]
            f1_diff = anonymization_labels[label][3] - baseline_labels[label][3]
            logging.info(f"Metric Differences for {label}:")
            logging.info(f"Accuracy Difference: {accuracy_diff:.4f}")
            logging.info(f"Precision Difference: {precision_diff:.4f}")
            logging.info(f"Recall Difference: {recall_diff:.4f}")
            logging.info(f"F1 Score Difference: {f1_diff:.4f}")
            logging.info("")

        # Calculate differences for overall metrics
        overall_accuracy_diff = anonymization_overall[0] - baseline_overall[0]
        overall_precision_diff = anonymization_overall[1] - baseline_overall[1]
        overall_recall_diff = anonymization_overall[2] - baseline_overall[2]
        overall_f1_diff = anonymization_overall[3] - baseline_overall[3]
        logging.info("Overall Metric Differences:")
        logging.info(f"Accuracy Difference: {overall_accuracy_diff:.4f}")
        logging.info(f"Precision Difference: {overall_precision_diff:.4f}")
        logging.info(f"Recall Difference: {overall_recall_diff:.4f}")
        logging.info(f"F1 Score Difference: {overall_f1_diff:.4f}")
        logging.info("")

        print(" --> Model evaluation saved to", log_filepath, "\n")
