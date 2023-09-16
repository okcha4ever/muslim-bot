# <u class="italic" >Instagram Islamic Bot </u>

This is an Instagram bot that publishes a post every 2 hours about a hadith in the Sunna of the prophet Mohammed (PBUH).

## Get Started on Your Machine:

<b style="color:red">Make sure you have Python3 installed </b>
Clone/Download the repository and run `pip3 install -r requirements.txt`

Creat a `config.py` file in the **/bots** directory and add these following variables to it with your credentials:

```python
INSTAGRAM_USERNAME = "{your_username}"
INSTAGRAM_PASSWORD = "{your_password}"
```

### Steps this bot goes through

1. When the 2-hour period is reached, the bot will execute the `main()` function in `main.py`.

2. It generates the data that gets drawn in the image from an api called **TextCortex AI** and format the data as python dictionary to access element inside (You can check out the prompt in `main.py`).

3. After the data in generated it gets sent to `draw.py` which will draw/write the data into a `e_post.jpg` file and saving it in `/media` directory.

4. After the image is saved, `draw.py` will call function inside `instagram.py` which will find the file and post it to Instagram

### Things might add to this:

- A telegram bot that tells me if the script ran or failed, if it succeeded: sends me the generated image and says so

### Folder Structure

`/bots`: has the bots that will do the uploading/sending
`/media`: has the the generated image `e_post.jpg`.
| -> `/fonts`: has used fonts

`Base Dir`: has the script that runs the bot
