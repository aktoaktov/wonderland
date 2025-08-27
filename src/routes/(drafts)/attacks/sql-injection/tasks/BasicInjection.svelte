<script>
    import Task from "$lib/kit/Tasks/Task.svelte"
    import Paragraph from "$lib/kit/Typography/Paragraph.svelte"
    import FormLayout from "$lib/kit/Forms/FormLayout.svelte"
    import Input from "$lib/kit/Forms/Fields/Input.svelte"
    import PasswordInput from "$lib/kit/Forms/Fields/PasswordInput.svelte"

    import initSqlJs from "sql.js"
    import Columns from "$lib/kit/Stencils/Columns.svelte"
    import DescList from "$lib/kit/Tables/DescList/index.js"
    import Row from "$lib/kit/Tables/DescList/Row.svelte"
    import Error from "$lib/kit/Stencils/Error.svelte"
    import Space from "$lib/kit/Elements/Space.svelte"
    import Code from "$lib/kit/Code/Code.svelte"
    import Icon from "$lib/kit/Elements/Icon.svelte"
    import Result from "$lib/kit/Code/Result.svelte"

    let db
    let result = []

    let name, password

    initSqlJs({locateFile: filename => `/${filename}`}).then(function (SQL) {
        // @formatter:off
        db = new SQL.Database()
        db.exec(`CREATE TABLE users (id INT,name TEXT, password TEXT, isadmin BOOLEAN)`)
        db.exec(`INSERT INTO users VALUES (1, "admin", "3fhgrfouhbc", true)`)
        db.exec(`INSERT INTO users VALUES (2, "vasya", "password", false)`)
        db.exec(`INSERT INTO users VALUES (3, "secretuser", "rgffuh32kgjhT", false)`)
    })

    const signin = () => {
        const data = db.exec(`SELECT * from users WHERE name = "${name}" AND password = "${password}"`)

        if (data.length === 0) result = null
        else result = data[0].values
    }
</script>

<Task number="1" heading="Базовая инъекция">
    <Paragraph>
        Перед вами имитация страницы входа на сайт. Для примера логин и пароль аккаунта без прав
    </Paragraph>
    <DescList>
        <Row term="Логин"><Code source="vasya"/></Row>
        <Row term="Пароль"><Code source="password"/></Row>
    </DescList>

    <Paragraph>
        Вам нужно зайти в аккаунт администратора и получить пароли <b>всех</b> пользователей.
    </Paragraph>

    <Columns>
        <FormLayout action="Войти" on:submit={signin}>
            <Input bind:value={name} label="Имя пользователя"/>
            <PasswordInput bind:value={password} label="Пароль"/>
        </FormLayout>

        <Space>
            {#if result === null}
                <Error heading="Такого пользователя не существует">
                    <Paragraph>Неправильное имя пользователя или пароль</Paragraph>
                </Error>
            {:else }
                {#each result as user}
                <Result>
                    <DescList>
                        <Row term="ID">{user[0]}</Row>
                        <Row term="Имя">{user[1]}</Row>
                        <Row term="Пароль">{user[2]}</Row>
                        <Row term="Админ?"><Icon name={user[3] ? "yes" : "no"}/></Row>
                    </DescList>
                </Result>
                {/each}
            {/if}
        </Space>
    </Columns>
</Task>