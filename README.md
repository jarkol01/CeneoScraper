# CeneoScraper

## Struktury oponii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|SKładowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|||
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|autor opinii|span.user-post__author-name|||
|rekomendacja autora|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|div.review-feature__col > review-feature__title--positives|||
|lista wad|div.review-feature__col > review-feature__title--negatives|||
|dla ilu osób przydatna|button.vote-yes > span|||
|dl ilu osób nieprzydatna|button.vote-no > span|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|||
|data zakupy produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|||

