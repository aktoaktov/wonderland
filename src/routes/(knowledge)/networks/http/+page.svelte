<script>
    import Title from "$lib/Elements/Title.svelte"
    import Section from "$lib/Markup/Section.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
</script>

<Title title="HTTP"
/>

<Section>
<Par>
    <P>
        <b>HTTP</b> (Hyper text transfer protocol) &mdash; прикладной протокол, на котором работает почти весь
        светский интернет.
    </P>
    <P>
        HTTP &mdash; протокол клиент-серверного взаимодействия. Клиентское приложение
        формирует запрос и отправляет его на сервер, сервер обрабатывает этот запрос, формирует ответ и передаёт его
        обратно клиенту.
    </P>
    <P>
        Клиент и сервер взаимодействуют, обмениваясь отдельными (абстрактными) сообщениями, а не потоком данных.
        Сообщения,
        отправляемые клиентом, называются <b>запросами</b> (request), а сообщения от сервера называются <b>ответами</b>
        (response).
    </P>
</Par>

<Subheading>HTTP-поток</Subheading>
<Par>
    <P>
        Клиент инициирует TCP-соединение с сервером, которое будет использоваться для обмена сообщениями. Клиент
        может открыть новое соединение или переиспользовать существующее.
    </P>
    <P>
        Клиент отправляет запрос, например
    </P>
    <Codeblock language="http"
               code={`GET / HTTP/1.1\nHost: google.com\nAccept-Language: ru`}/>
    <P>
        Клиент получает, читает и интерпретирует ответ от сервера, например
    </P>
    <Codeblock language="http"
               code={`HTTP/1.1 200 OK\nDate: Sat, 18 Jan 2025 20:42:37 GMT\nServer: gws\nContent-Length: 67989\nContent-Type: text/html\n\n<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ru"><head>...`}/>
</Par>

<Par>
    <P>Любое HTTP-сообщение состоит из трех частей: стартовая строка, заголовки и тело.</P>
    <P>
        Стартовая строка отличается у запросов и у ответов. <br/>
        У запроса это строка <Code c="Method URI"/> для версии протокола 0.9 и <Code c="Method URI HTTP/Version"/> для
        других версий. <br/>
        У ответа это строка <Code c="HTTP/Version StatusCode Reason"/>.
    </P>
    <P>
        <Code c="Method"/> &mdash; метод запроса,<br/>
        <Code c="URI"/> &mdash; идентификатор запрашиваемого ресурса,<br/>
        <Code c="Version"/> &mdash; версия протокола HTTP,<br/>
        <Code c="Status Code"/> &mdash; код состояния, кратко сообщающий о результате запроса,<br/>
    </P>
</Par>
</Section>

<Section>
<Heading>Методы запросов</Heading>
<Par>
    <P>
        <b>Метод</b> (method) запроса определяет операцию, которую надо совершить над ресурсом.
    </P>
    <P>
        Метод является <b>идемпотентным</b>, если повторный идентичный запрос никак не изменит состояние сервера.
        Единственное жесткое требование к методам &mdash; их идемпотентность. Остальное закреплено только на уровне
        соглашений, которые очень желательно соблюдать. Хотя никто строго не запрещает использовать
        метод <Code c="GET"/> для удаления ресурсов, и никто не мешает придумать собственный
        метод <Code c="KRUCFYI"/>.
    </P>
</Par>

<Subheading>GET</Subheading>
<Par>
    <P>Метод <Code c="GET"/> используется для получения ресурсов.</P>
</Par>
</Section>
