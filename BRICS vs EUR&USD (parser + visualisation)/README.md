# Сбор валют из Центрального Банка и визуализация полученных данных

## Была написана программа, собирающая курсы валют из ЦБ и сохраняющая их в базе данных. После чего данные были визуализированы в виде дашборда.

Про стек:  
- **Python** с библиотеками `request`, `BeautifulSoup`, `SQLAlchemy`. 
Первые две библиотеки позволили успешно запарсить валюты, а последняя правильно их упаковать в базу данных
- **PostgreSQL** использовался для хранения 
- **Tableau** для визуализации 

![Dashboard 2](https://github.com/user-attachments/assets/ffd792c5-47f5-4635-a6cd-991313570c80)


<div class='tableauPlaceholder' id='viz1732794669460' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;cu&#47;currency_17327937719460&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='currency_17327937719460&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;cu&#47;currency_17327937719460&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1732794669460');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1440px';vizElement.style.height='817px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1440px';vizElement.style.height='817px';} else { vizElement.style.width='100%';vizElement.style.height='1577px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
