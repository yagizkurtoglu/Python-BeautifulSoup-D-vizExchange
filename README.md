# Python-BeautifulSoup-DovizExchange
Python BeautifulSoup kütüphanesi ile Döviz Exchange  Uygulaması

<p>Uygulama web sitesine bağlanmak i&ccedil;in&nbsp;<strong>requests</strong> verileri &ccedil;ekmek i&ccedil;in ise&nbsp;<strong>BeautifulSoup</strong> k&uuml;t&uuml;phanelerini kullanır.</p>
<ul style="list-style-type: circle;">
<li>Veriler doviz.com sitesinden alınır.&nbsp;</li>
<li>Uygulamanın başında kullanılabilecek d&ouml;viz t&uuml;rleri aşağıdaki gibi listelenir.&nbsp;</li>
<li>['USD', 'EUR', 'GBP', 'CHF', 'CAD', 'RUB', 'AED', 'AUD', 'DKK', 'SEK', 'NOK', 'JPY', 'KWD', 'ZAR', 'BHD', 'LYD', 'SAR', 'IQD', 'ILS', 'IRR', 'INR', 'MXN', 'HUF', 'NZD', 'BRL', 'IDR', 'CSK', 'PLN', 'RON', 'CNY', 'ARS', 'ALL', 'AZN', 'BAM', 'CLP', 'COP', 'CRC', 'DZD', 'EGP', 'HKD', 'HRK', 'ISK', 'JOD', 'KRW', 'KZT', 'LBP', 'LKR', 'MAD', 'MDL', 'MKD', 'MYR', 'OMR', 'PEN', 'PHP', 'PKR', 'QAR', 'RSD', 'SGD', 'SYP', 'THB', 'TWD', 'UAH', 'UYU', 'GEL']N', 'PHP', 'PKR', 'QAR', 'RSD', 'SGD', 'SYP', 'THB', 'TWD', 'UAH', 'UYU', 'GEL']</li>
<li>Daha sonra sırasıyla Bozulan D&ouml;viz T&uuml;r&uuml; , Alinan D&ouml;viz T&uuml;r&uuml; ve Miktar bilgileri kullanıcıdan istenir.&nbsp;</li>
<li>Uygulamayı girdiler sırasıyla USD EUR 100 olarak test edersek aşağıdaki &ccedil;ıktıyı verecektir.</li>
<li>*******<br />1 USD = 0.8966 EUR<br />100 USD = 89.6638 EUR<br />*******</li>
</ul>
<ul>
<li>D&ouml;viz tipleri dictionary veri tipi ile tutulmaktadır. {name:value, ... }</li>
</ul>
<div>&nbsp;</div>
