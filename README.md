# square_transaction_parser
If you own a business or do some on the side work you might use square or square invoices. One of the frustrating things about square is it's reporting.

While all transactions are reportable and can be exported via a csv file, it's kind of a messy file and doesn't make it easy to import.

## Method logic

I like to track my processing fees inside my preferred accounting program, in my case, GNU Cash. The problem is when importing
just my bank account, I only see the deposit, not the fee. There are manual ways, and some paid ways, to import the processing fees, but it's
easy to do this with a simple script. 

The script goes through each line of a square transcation CSV and does the following:

- Removes all the extra data we don't need
- Adds 2 additional transactions
- Adds account information for GNU Cash to use

First we get rid of all the data we don't need, stuff like the transcation codes, card types, timestamp, etc. We keep the data, gross amount, net ammount,
fee, and total.

Then we add in an additional transaction. This transaction accounts for the transfer between the square and your bank. 

Finally, we add in another transaction for the square fees as an expense account.

Please Note: It is rare for me to receive a deposit with multiple sales in a single day, use caution as this is UNTESTED. I highly recommend setting up 
a test GNU Cash file to ensure success before messing with your live file and importing the data.

## Accounting explaination

The basic idea here is:

- Income gets recorded to a square holding account
- A transfer is reported between square and your bank account
- A record is created to record the fee in your expense account. 

If you're an accountant and think I'm going about this wrong, please tell me, I'd love to learn best practices to keep myself and others
out of trouble.

## To use
You'll need python 3 to get started. Python is cross plateform and easy to install on most operating systems. 

Open up python 3 and edit the variables at the top. These variables are documented in the script file itself.
Adjust your script for the accounts you have setup in GNU Cash for your bank, square holding account, and your expense account for square fees.

Place a square transaction csv file in the directory with the script, ensuring it is named in the script variable, and run it. You can run it by
either doubleclicking or using a command prompt. On windows  "python script.py" If running via doubleclick, it's perfectly normal on windows to see
the command propt flash on the screen for a second. As long as you see the new csv, it worked just fine.

You should see your new file in the directory.

If you don't see it appear, there may be an error. Run the script via a command prompt and you'll be able to see the error.

## Final thoughts

This is a very simple script and it can probably be made to work with Stripe or Paypal csvs as well. I'll likely be porting this to work with Stripe
very soon as I'm migrating to a new invoicing plateform soon for my business. 

I'm pretty new to scripting something like this and python in general. I only share this here because I had a need for it and I thought it would be 
a good learning experience. If you find it useful, please let me know. If your a pro at python and I did something wrong, feel free to share.

Finally, I'd REALLY like to thank all those on forums such as stackoverflow for answering questions. Google leads us to answers when we can't figure
something out and if it were not for the people on these forums answering questions, I'd probably never be able to learn anything at all... literally nothing!

## Support

I don't support this directly but will try to help if I can. No warranty is guarenteed, 
KEEP A BACKUP OF YOUR DATABASE AND YOUR CSV FILES!
