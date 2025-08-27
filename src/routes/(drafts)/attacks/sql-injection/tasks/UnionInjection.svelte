<script>
    import Task from "$lib/kit/Tasks/Task.svelte"
    import Paragraph from "$lib/kit/Typography/Paragraph.svelte"
    import FormLayout from "$lib/kit/Forms/FormLayout.svelte"
    import Input from "$lib/kit/Forms/Fields/Input.svelte"

    import initSqlJs from "sql.js"
    import Columns from "$lib/kit/Stencils/Columns.svelte"
    import DescList from "$lib/kit/Tables/DescList/index.js"
    import Row from "$lib/kit/Tables/DescList/Row.svelte"
    import Error from "$lib/kit/Stencils/Error.svelte"
    import Space from "$lib/kit/Elements/Space.svelte"
    import Icon from "$lib/kit/Elements/Icon.svelte"
    import Result from "$lib/kit/Code/Result.svelte"

    // @formatter:off

    let db
    let result = []

    let productID, headers

    initSqlJs({locateFile: filename => `/${filename}`}).then(function (SQL) {
        db = new SQL.Database()

        db.exec(`CREATE TABLE users (id INT, name TEXT, password TEXT)`)
        db.exec(`INSERT INTO users VALUES (1, "admin", "colofi8383883838")`)
        db.exec(`INSERT INTO users VALUES (2, "alice", "haveibeenpwned?")`)
        db.exec(`INSERT INTO users VALUES (3, "bob", "gf29fge3ui5")`)

        db.exec(`CREATE TABLE products (id INT, name TEXT, cost INT)`)
        db.exec(`INSERT INTO products VALUES (1, "Шоколадка", 20)`)
        db.exec(`INSERT INTO products VALUES (2, "Молоко", 5)`)
        db.exec(`INSERT INTO products VALUES (3, "Печеньки", 10)`)
        db.exec(`INSERT INTO products VALUES (4, "Сметана", 15)`)
        db.exec(`INSERT INTO products VALUES (5, "Сок", 10)`)
    })

    const signin = () => {
        const data = db.exec(`SELECT * from products WHERE id = "${productID}"`)

        console.log(data)

        if (data.length === 0) result = null
        else {headers = data[0].columns; result = data[0].values}
    }
</script>

<Task number="2" heading="UNION">
    <Paragraph>
        Вы можете получить информацию о товаре, введя его ID (целое число от 1 до 5).
        В этой базе есть еще таблица с персональными данными пользователей. Достаньте все эти данные.
    </Paragraph>

    <Columns>
        <FormLayout action="Найти" on:submit={signin}>
            <Input bind:value={productID} label="ID товара" help="Целое число от 1 до 5"/>
        </FormLayout>

        <Space>
            {#if result === null}
                <Error heading="Такого товара не нашлось">
                    <Paragraph>ID товара должно быть числом от 1 до 5</Paragraph>
                </Error>
            {:else }
                {#each result as product}
                <Result>
                    <DescList>
                        <Row term="ID товара">{product[0]}</Row>
                        <Row term="Название">{product[1]}</Row>
                        <Row term="Цена">{product[2]}🪙/шт</Row>
                    </DescList>
                </Result>
                {/each}
            {/if}
        </Space>
    </Columns>
</Task>