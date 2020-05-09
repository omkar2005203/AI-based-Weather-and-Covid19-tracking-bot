# AI-based-Weather-and-Covid19-tracking-bot
This is AI based bot to track weather around world and get count of covid19 infected people in India statewise..

1) Modify telegram bot api token and open weather token in globalConfigs.py

2) main single file to run chabot is vc_telegram.py

3) "trained" folder contains rasa trained nlu models (you can open it separtely to train rasa nlu model)
 In folder data.json is used for training data.To launch rasa GUI based nlu trainer command : rasa-nlu-trainer 
 before training we need to convert  .json to .md and copy data of .md file to nlu file then use command rasa train.
