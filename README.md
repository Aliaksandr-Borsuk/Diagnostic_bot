## Diagnostic_bot
The bot generates a list of probable diagnoses
# !!! WARNING !!!
**You can use the results of this bot only for educational purposes.**   
**The diagnoses and prescriptions that this bot makes are not medical diagnoses and not medical prescriptions.**
  
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
📁 predicting_the_disease_by_symptoms    <br />
 |_ $\space$ bot.py  <br />
 |_ $\space$ .env  <br />
 |_ $\space$ .env.example  <br />
 |_ $\space$ .gitignore  <br />
 |_  📁 data  <br />
 | $\space\space\space$  |_ $\space$ book.txt  <br />
 |_ 📁 config_data  <br />
 | $\space\space\space$   |_ $\space$config.py  <br />
 |_ 📁 database  <br />
 |  $\space\space\space$  |_ $\space$ users_database.py   <br />
 |  $\space\space\space$  |_ $\space$ model_    <br />
 |_ 📁 filters  <br />
 |   $\space\space\space$ |_ $\space$ filters.py  <br />
 |_ 📁 handlers  
 |  $\space\space\space$  |_ $\space$ other_handlers.py  <br />
 |  $\space\space\space$  |_ $\space$ user_handlers.py  <br />
 |_ 📁 keyboards  <br />
 |   $\space\space\space$ |_  $\space$ bookmarks_kb.py  <br />
 |   $\space\space\space$ |_  $\space$ main_menu.py  <br />
 |   $\space\space\space$ |_  $\space$ pagination_kb.py  <br />
 |_ 📁 lexicon  <br />
 |  $\space\space$$\space$  |_  $\space$ lexicon.py  <br />
 |_ 📁 services  <br />
    $\space\space\space\space\space$  |_  $\space$ file_handling.py   <br />
</details> 

