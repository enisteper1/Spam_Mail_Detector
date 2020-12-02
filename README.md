# Introduction
<p>This Project reads your mails from your gmail address and tells if they are spam or not.</p>
<p>For training from https://www.kaggle.com/uciml/sms-spam-collection-dataset <strong> spam.csv </strong> dataset and <strong>Logistic Regression</strong> algorithm is used.</p>

# Usage
<p>At first Gmail Api is required to be activated by following steps at https://developers.google.com/gmail/api/quickstart/python . Running quickstart.py is not necessary</p>
<p>After activating your gmail api put <strong>credentials.json</strong> file into this folder.</p>
<p>Finally run <strong>python main.py </strong> to train the model and save the both weights and data. </p>
<p>Additionally the <strong>last</strong> parameter decides the how many data will be taken for prediction, by default it is 5.</p>

# Example
`python main.py --last 7`

<strong>
 Yes i have. So that&#39;s why u texted. Pshew...missing you so much is  NOT SPAM

 REMINDER FROM O2: To get 2.50 pounds free call credit and details of great offers pls reply 2 this text with your valid name, house no and postcode is  SPAM!

 Rofl. Its true to its name is  NOT SPAM

 I&#39;m leaving my house now... is  NOT SPAM

 Sunshine Quiz Wkly Q! Win a top Sony DVD player if u know which country the Algarve is in? Txt ansr to 82277. 1.50 SP:Tyrone is  SPAM!

 K. Did you call me just now ah? is  NOT SPAM

 07732584351 - Rodger Burns - MSG = We tried to call you re your reply to our sms for a free nokia mobile + free camcorder. Please call now 08000930705 for delivery tomorrow is  SPAM!
</strong>
