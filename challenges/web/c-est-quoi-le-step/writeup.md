# C'est quoi le STEP?

## Write-up

Upon arrival, the page showed lots of possible definition for the acronym. Only one of those definition was greyed out, `Service Télématique des Étudiants de Polytechnique`, that was indeed the true answer. But that did not give you anything. The "admin" tab was where the flag was located. 

However, you could not access the admin page, who granted you with "External connection detected, access forbidden! This incident will be reported" on a 403 Forbidden page.

### Where *is* the STEP?

The only university mentionned in all the possible definition was Polytechnique. With a quick web search for "STEP Polytechnique", you could find a website with the URL `step.polymtl.ca`. You could read on the website (and English-speaking folks could [translate the website](https://step-polymtl-ca.translate.goog/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=fr&_x_tr_pto=wapp)) that the STEP had their own servers.

Using the Internet Systems Consortium DNS lookup utility `host`, you could find the address of such website.

```bash
$ host step.polymtl.ca
step.polymtl.ca has address 132.207.31.42
step.polymtl.ca mail is handled by 0 zimbra-recovery.step.polymtl.ca.
```

Polytechnique Montreal like all Quebec university is located inside the RISQ (*Réseau d'informations scientifiques du Québec*) whose network is `132.0.0.0/8`. For example, the IP Address of `concordia.ca` is `132.205.244.185`. Upon looking up domain `polymtl.ca`, you also learned that Polytechnique Montreal servers are in the `132.207.0.0/16` network. Hereafter, you could easily find that STEP's servers are in the `132.207.31.0/24` network.

### `X-Forwarded-For` Header

If you send a `GET` request to the server with the `X-Forwarded-For` header assigned to an IP in the STEP's network (i.e. `132.207.31.*`), the server returns a page with the flag

### What *is* the STEP?

The STEP is an cloud infrastructure and web services club at Polytechnique Montreal. You can sign up to its [GitLab Ultimate Instance](git.step.polymtl.ca) free of charge with an e-mail address from any Quebec university and contribute to FLOSS projects.

## Flag

`flag{C0ngr4ts!!H4cker!pLeAsEcOnSiDeRcOnTrIbUtInGtOgIt.StEp.PoLyMtL.cA}`