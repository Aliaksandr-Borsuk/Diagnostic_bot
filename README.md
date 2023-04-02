## Diagnostic_bot
The bot generates a list of probable diagnoses
# !!! WARNING !!!
**You can use the results of this bot only for educational purposes.**   
**The diagnoses and prescriptions that this bot makes are not medical diagnoses and not medical prescriptions.**
   
Read this in other languages: **to do Russian**
  
## What can this bot do ?
  
<details>   
 <summary>clik here </summary>  
 - This bot can predict probable diseases based on symptoms.<br />
 - This bot can also show a description of the disease and prescriptions.  <br />
</details>   

## What can't this bot do?  

<details>    
 <summary>clik here </summary>  
 - The bot has only 40 diagnoses. The bot cannot make a diagnosis that is not in its data. <br />  
 - The bot uses a toy database and cannot save user data yet. <br />
 - Also, while the bot can only communicate in English. <br />
</details> 
  
## Description of interaction with the bot.  
  
<details>    
 <summary>clik here </summary>  
 - The user sends the /start command to the bot (or starts it by finding it in the search) <br />  
 - The bot informs the user that the diagnoses are not medical diagnoses and offers to start diagnostics. <br />
 - If the user sends the /run_diagnostics command, the bot prompts the user to select symptoms. <br />
 - -  the user can add or remove symptom by clicking on it. <br />
 - -  the list of symptoms is displayed above the inline keyboard. <br />
 - -  the symptoms are sorted alphabetically, and the user can select the pages of symptoms with the buttons <b><<</b> and <b> >> </b> <br />
 - if the user clicks on the <b>Get diagnosis</b> button, the bot will send a list of possible diagnoses. <br />
 - if the user clicks on the button with the name of the diagnosis, the bot will send a description of the disease and prescriptions. <br />
</details> 
</b>
  
## The structure of the Diagnostic_bot
  
<details>    
 <summary>clik here </summary>  
📁 diagnostic_bot    <br />
 |_ $\space$ bot.py  <br />
 |_ $\space$ .env  <br />
 |_ $\space$ .env.example  <br />
 |_ $\space$ .gitignore  <br />
 |_ 📁 config_data  <br />
 | $\space\space\space$   |_ $\space$ config.py  <br />
 |_  📁 data  <br />
 | $\space\space\space$  |_ $\space$ my_symptom_Description.csv  <br />
 | $\space\space\space$  |_ $\space$ my_symptom_precaution.csv <br />
 | $\space\space\space$  |_ $\space$ my_symptoms_of_diseases.csv  <br />
 | $\space\space\space$  |_ $\space$ my_symptom_Description.csv  <br />
 |  $\space\space\space$  |_ $\space$ model   <br />
 |_ 📁 database  <br />
 |  $\space\space\space$  |_ $\space$ users_database.py   <br />
 |_ 📁 filters  <br />
 |   $\space\space\space$ |_ $\space$ filters.py  <br />
 |_ 📁 functions  <br />
 |   $\space\space\space$ |_ $\space$ handlers_funcsions.py  <br />
 |_ 📁 handlers  <br />
 |  $\space\space\space$  |_ $\space$ other_handlers.py  <br />
 |  $\space\space\space$  |_ $\space$ user_handlers.py  <br />
 |_ 📁 keyboards  <br />
 |   $\space\space\space$ |_  $\space$ main_menu.py  <br />
 |   $\space\space\space$ |_  $\space$ keyboards.py  <br />
 |_ 📁 lexicon  <br />
 |  $\space\space\space$  |_  $\space$ lexicon_en.py  <br />
 |_ 📁 services  <br />
    $\space\space\space\space\space$  |_  $\space$ file_handling.py   <br />
</details> 
  
## Description of the bot structure
<details>   
 <summary>clik here </summary>  
📁 diagnostic_bot - the root directory of the entire project <br />
bot.py - the main executable file
.env - the file with environment variables (secret data) for the bot configuration
.env.example - the file with examples of secrets for GitHub
.gitignore - which files and directories not to track
📁 config_data - directory with the bot configuration module
config.py - module for bot configuration
📁 database - the package for working with a database
database.py - the module with a template of our "toy" database
📁 filters - the package with filters
filters.py - the module with filters 
📁 handlers - the package with handlers
other_handlers.py - the module with a handler for any user messages
user_handlers.py -  the module with user handlers
📁 keyboards - the package with bot keyboards
main_menu.py - the module for forming the main menu of the bot
keyboards.py - the module for forming another keyboards
📁 lexicon - the directory for storing bot dictionaries
lexicon_en.py - the file with a dictionary
📁 services - a package with auxiliary tools for the work of the bot
file_handling.py - a module for preparing data
</details> 
