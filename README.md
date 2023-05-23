# Observabilidade - Light House

> Projetc Samsung with Elasticsearch

## Note

> This program sends a **_JSON_** with pageSpeed information (URL performance) of various URLs to Elasticsearch.
> You need knowledge about Elasticsearch and Index to get the most out of them.
> We assume that you already know how requests work.
> For it to work, you'll need to make a few small tweaks to your business.

## Create .env

> 1. Create a key at *https://developers.google.com/speed/docs/insights/v5/get-started* to get access to pagespeed.
> 2. Create an _.env_ file in the root directory.
> 3. In the variable **_PAGE_SPEED_URL_API_** you must put the following link: *https://www.googleapis.com/pagespeedonline/v5/runPagespeed*
> 4. In the **_CAPTCHA_TOKEN_** variable you must add the token you received from the PageSpeed API.
> 5. **_ELASTIC_URL_API_** must be a submission URL for Elasticsearch.
> 6. **_AUTH_USER_** and **_AUTH_PASS_** must be created within Elasticsearch with admin or superadmin permission.

# How JSON is Constructed

> We have a file called _pagespeed.json_ that gathers part of what we are going to send to Elasticsearch, we also get the 6 metrics that make up Light House plus the page score, which are:

> 1. first-contentful-paint
> 2. interactive
> 3. speed-index
> 4. total-blocking-time
> 5. largest-contentful-paint
> 6. cumulative-layout-shift
> 7. Socre (Plus)

> ## Note

> > > There are other metrics on pageSpeed, but we are limiting the 6 main metrics, to learn more visit the link *https://developers.google.com/speed/docs/insights/v5/about*

> In the _pagespeed.json_ file we must create it according to the following pattern:

> > [{"url":"https://www.google.com.br/"},{"url":"https://www.google2.com.br/"}]

> or

> > [{"url":"https://www.google.com.br/", "menu": "menu name"}, {"url":"https://www.google2.com.br/ ", "menu": "menu name"}]

> for URLs that have categories or subcategories or that are inside menus.

> ## Note

> > The URL parameter is mandatory for the program to work correctly.
