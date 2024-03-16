const port = 8000;

const flag1 = "flag{this-book-is-about-MS-Azure-right?-https://hubertreeves.info/livres/patience.html}"
const flag2 = "flag{waiting-for-godot}"
const flag3 = "flag{puzzle-heros-are-idle-games-now}"

const first_delay = 1000 * 60 * 3
const other_delays = 1000 * 60 * 5


const express = require('express')
const cookieParser = require('cookie-parser')

//setup express app
const app = express()

// lets you use the cookieParser in your application
app.use(cookieParser());

app.use(function (req, res, next) {
    console.log('intercept')
    req.setTimeout(10 * 60 * 1000 * 2);

    next();
});


app.set('trust proxy', true);

function handler(req, res) {

    let randomId = Math.floor(Math.random() * 4503599627370496);
    let id = `${req.ip}-${randomId}`;

    console.log(new Date(), `connected ${id}`);

    // *Message complexe* si vous acceptez les termes et conditions, ajoutez "i=understand" aux paramètres de la requêtes
    const query1_ok = "status" in req.query && req.query["status"] == "accept"

    // User-agent
    const user_agent1_ok = 'user-agent' in req.headers && req.headers['user-agent'].indexOf('Firefox/114.0') !== -1
    const user_agent2_ok = 'user-agent' in req.headers && req.headers['user-agent'].indexOf('Windows Phone') !== -1

    // I'm sorry, this website is only compatible with the navigator Firefox 114.0
    const user_agent_ok = user_agent1_ok || user_agent2_ok

    // If you consent XYZ, add a cookie
    const cookie_ok = 'READY' in req.cookies && req.cookies['READY'] == 'YESSIR'

    // It's dangerous out there! We should use some access authentication... Doesn't have to be complex, a basic one would be fine admin / secret
    const basic_http_auth_ok = "authorization" in req.headers && req.headers["authorization"] == 'Basic YWRtaW46c2VjcmV0'

    // Have you been implicitly authorizing websites to track you all this time???? Are you insane??? If you don't want to be tracked, you should say it
    const dnt_ok = !!(+req.headers["dnt"])

    // Warum würdest du Deutsch nicht als Sprache akzeptieren?
    const accept_language_de_ok = "accept-language" in req.headers && req.headers["accept-language"].indexOf('de') !== -1

    // Actually I changed my mind, I think you should browse this site using a Windows Phone
    user_agent2_ok;

    const accept_gzip_ok = "accept-encoding" in req.headers && req.headers["accept-encoding"].indexOf('gzip') !== -1

    // I feel like this query should have come from perdu.com
    const referer_ok = "referer" in req.headers && req.headers["referer"].indexOf('perdu.com') !== -1

    // You sure like to get a lot, but could you put instead?
    const put_method_ok = !!req.route.methods.put

    // If you've been this far and you still want to get the flag, add "..." to your query
    const query2_ok = false


    let message;
    let delay = other_delays;

    if(!query1_ok) {

        delay = first_delay;
        message = `
Hi! Welcome to my super website! It's hosted on my very own Raspberry Pi, in my mom's basement. My mom is very proud of me

If you wish to continue, you have to accept the terms and conditions that my mom established :

- No loud music after 22:00
- Finish the dishes before playing to the PS4
- That's it for now but there might be more rules in the future


If you accept those terms and conditions, please add status=accept to your query arguments.



Sorry about that lag btw, my server can be slow from time to time.

Here is a little flag for your trouble ${flag1}

        `.trim();
    } else if(!user_agent_ok) { // ni Firefox, ni Windows Phone

        delay = other_delays;

        message = `
I'm sorry, this website is only compatible with the navigator Firefox 114.0

I really should update that at some point, maybe later
        `.trim();
    } else if(!cookie_ok) {

        delay = other_delays * 2;

        message = `
All right, looks like we can start!

Are you ready? If so, you should add a new cookie called READY with the value YESSIR
        `.trim();
    } else if(!basic_http_auth_ok) {

        delay = other_delays * 3;

        message = `
ALL RIGHT! I'M REAAAAAAAADY! Here's the second flag: ${flag2}

And the third one is... Wait... How can I make sure that I'm really talking to you?

We should use some kind of authentication. Any one would do, but I'd rather not use anything too complex. A basic one would do.

If you're really yourself, authenticate yourself. This is your encrypted ID:

hfre: nqzva // cnff: frperg
        `.trim();
    } else if(!dnt_ok) {

        delay = other_delays * 4;

        message = `
Ok so, the next flag is...

Wait, have you been implicitly authorizing websites to track you all this time???? Are you insane??? I can't in good conscience give the flag to someone that tacitly accepted such barbarous practices
        `.trim()
    } else if(!accept_language_de_ok) {

        delay = other_delays * 5;

        message = `
Warum würden Sie Deutsch nicht als Sprache akzeptieren? Die Flagge ist möglicherweise auf Deutsch, was weiß ich?
        `.trim()
    } else if(!user_agent2_ok) {

        delay = other_delays * 6;

        message = `
Actually I changed my mind, Firefox is lame. I think you should browse this site using a Windows Phone
        `.trim()
    } else if(!accept_gzip_ok) {

        delay = other_delays * 7;

        message = `
Ok, so the flag is...

You know, I thinking of compressing my messages from now on, what do you think about that?
I guess if you can't read compressed messages, there's no use in talking to you
        `.trim()
    } else if(!put_method_ok) {

        delay = other_delays * 8;

        message = `
I think I'm still not ready to tell you the flag... Should I really trust you?

From the beginning of our relationship, everything you ever did was to GET things from me.
Couldn't you PUT in a little of yourself in this relationship for once?
        `.trim()
    } else if(!referer_ok){

        delay = other_delays * 9;

        message = `
Ok, ok, one last thing and I swear I'm giving you your flag.

My favorite webiste of all time is http://perdu.com/

Before we part ways, could you go there and then come back here? If you're lost, ask them nicely to get you back here
        `.trim()
    } else {
        delay = 1;

        message = `
Thank you for all those precious hours we spent together, I'll cherish those memories forever

${flag3}
        `.trim();
    }

    // The Puzzle Hero Firewall Gods must be pleased
    delay = Math.min(delay, 1000 * 60 * 19.5);

    let timeoutAnswer = setTimeout(() => {
        console.log(new Date(), `data sent ${id}`);
        res.set('Content-Type', 'text/plain')
        res.send(message + '\n');
    }, delay);


    req.on('close', function() {
        console.log(new Date(), `closed ${id}`);
        clearTimeout(timeoutAnswer);
    });
};

//set a simple for homepage route
app.get('/', handler);
app.put('/', handler);


let server = app.listen(port, () => console.log('Started'));
server.setTimeout(other_delays * 2);
