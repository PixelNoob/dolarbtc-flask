# El dolarbtc-flask

El Bitcoin se intercambia de forma libre los 7 días de la semana y sin restricciones gubernamentales, por lo que el “Dólar Bitcoin” es considerado un índice indicativo del precio real del dólar en Argentina.

El Precio del Dólar Bitcoin se obtiene dividiendo el precio de venta de Bitcoin en Argentina por el Precio Internacional de Bitcoin. La formula es sencilla: 

    Precio de venta de Bitcoin en Argentina / Precio internacional del Bitcoin

Dolarbtc-flask busca de forma automatica el precio de las últimas ofertas de compra y venta de Bitcoins en el mercado Argentino, las promedia y divide el resultado por el valor actual del Bitcoin en dólares estadounidenses.  

API

el endpoint /api mantiene una api actualizada para desarrolladores, la misma se encuentra en formato json y se actualiza cada minuto. 

Una versión en vivo de esta app se encuentra alojada en [eldolarbtc.com](https://eldolarbtc.com)
