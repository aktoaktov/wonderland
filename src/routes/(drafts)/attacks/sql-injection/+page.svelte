<script>
    import Section from "$lib/kit/Typography/Section.svelte"
    import Contents from "$lib/kit/Layout/Contents.svelte"
    import OList from "$lib/kit/Lists/EnumList.svelte"
    import Item from "$lib/kit/Lists/Item.svelte"
    import Link from "$lib/kit/Elements/Link.svelte"
    import Title from "$lib/kit/Elements/Title.svelte"
    import Heading from "$lib/kit/Typography/Heading.svelte"
    import Codeblock from "$lib/kit/Code/Codeblock.svelte"
    import CodePart from "$lib/kit/Code/CodePart.svelte"
    import Paragraph from "$lib/kit/Typography/Paragraph.svelte"
    import Code from "$lib/kit/Code/Code.svelte"
    import C from "$lib/kit/Code/grammars/c.js"
</script>

<Title title="SQL инъекции"/>

<Contents>
    <OList>
        <Item>
            <Link to="#introduction" colorless>Введение</Link>
        </Item>
    </OList>
</Contents>

<Section>
    <Heading anchor="introduction">Введение</Heading>

    <Paragraph>
        Самая простая для понимания и не самая простая для реализации (в современных реалиях) уязвимость - SQL инъекция.
        Часто обзывается просто как SQLi (от SQL injection).
        Возникает эта уязвимость там, где вводятся какие-то данные: пароли, комментарии, ID новостей и т.д.
    </Paragraph>
    <Paragraph>
        Конкретно для HTTP ее стоит искать в различных полях URI, заголовках и телах запроса.
        Это - отправная точка дальнейшего тестирования.
        Мы будем изменять нормальные параметры, чтобы узнать как работает сервис и осуществить атаку.
    </Paragraph>

    <Paragraph>Здесь изменяемые поля прямо в URI</Paragraph>

    <Codeblock>
        <CodePart language="http" source="GET https://example.com/news?id=8128 HTTP/1.1"/>
    </Codeblock>

    <Codeblock>
        <CodePart language="http" source={`POST https://example.com/auth?username=jacob43&password=gfh3oEi HTTP/1.1`}/>
    </Codeblock>
    
    <Paragraph>А здесь - в теле запроса</Paragraph>

    <Codeblock>
        <CodePart language="http"
                  source={`POST https://example.com/auth HTTP/1.1\n
Host: example.com
User-Agent: Mozilla/5.0 (U; Linux i540) Gecko/20100101 Firefox/49.3
Accept: application/json
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br

`}/>
        <CodePart language="json" source={`{username: "jacob43", password: "gfh3oEi"}`}/>
    </Codeblock>

    <Paragraph>
        Когда бекенд плохо написан, данные подставляются прямо в строку запроса без предварительной фильтрации.
        Обычный цифирки и буковки навредить запросу не смогут, а специальные символы, которые являются частью SQL - вполне.
    </Paragraph>

    <Paragraph>
        Самый простой и банальный пример - запрос авторизации. Вариант <b>плохого</b> кода на бекенде, который выполняет этот запрос.
    </Paragraph>

    <Codeblock>
        <CodePart language="python" source={`db.execute('SELECT * FROM users WHERE'\n          f'username="{username}" AND password="{password}"')`}/>
    </Codeblock>

    <Paragraph>
        При нормальном запросе переменные <Code source="username"/> и <Code source="password"/> хранят нормальные данные, например <Code source="VasyaPupkin"/> и <Code source="HG7F3tfHGr6"/>.
        Эти данные поставятся в код, и запрос к базе данных будет выглядеть так
    </Paragraph>

    <Codeblock>
        <CodePart language="sql" source={`SELECT * FROM users WHERE username="VasyaPupkin" AND password="HG7F3tfHGr6"`}/>
    </Codeblock>

    <Paragraph>
        Если имя пользователя и пароль верные, то такой запрос вернет нормальную строку с данными Васи Пупкина.
    </Paragraph>

    <Paragraph>
        Что будет, если в переменных будут строки, содержащие синтаксис SQL?
        Здесь мы никак не проверяем и не обрабатываем эти строки, поэтому они прямо в исходном виде попадут в запрос.
        Попробуем получить доступ к админке.
    </Paragraph>

    <Paragraph>
        Пусть мы знаем, что имя учетной записи админа - <Code source="admin"/>.
        Тогда <Code language="sql" source={`username="admin"`}/>, и нам всего лишь нужно отключить проверку пароля.
        Для этого нужно закрыть кавычку и вставить символы комментариев <Code source="--"/>.
        Получаем, что в качестве имени пользователя выступает <Code source={`admin" --`}/>.
        Тогда запрос к базе данных при таких входных выглядит так
    </Paragraph>

    <Codeblock>
        <CodePart language="sql" source={`SELECT * FROM users WHERE username="admin" --" AND password="..."`}/>
    </Codeblock>

    <Paragraph>
        Этот запрос вернет данные админа, поскольку никаких проверок пароля не происходит.
        В этих данных может быть токен авторизации. Вуаля, вы теперь админ и можете творить все, что угодно.
        Учтите, что область применения не ограничивается только на входе в учетную запись админа.
    </Paragraph>

    <Paragraph>
        Цель большинства SQL-инъекций - изменить запрос к базе данных и вытащить нужные данные.
    </Paragraph>

    <Paragraph>
        Как с этим бороться? Писать нормальный код.
        И не стоит добавлять проверки на символы - этот трюк (возможно) прокатит с именами и паролями, но, например, с комментариями нет.
    </Paragraph>
</Section>