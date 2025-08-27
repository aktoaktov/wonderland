<script>
    import Section from "$lib/kit/Typography/Section.svelte"
    import Contents from "$lib/kit/Layout/Contents.svelte"
    import OList from "$lib/kit/Lists/EnumList.svelte"
    import Item from "$lib/kit/Lists/Item.svelte"
    import Link from "$lib/kit/Elements/Link.svelte"
    import Title from "$lib/kit/Elements/Title.svelte"
    import Heading from "$lib/kit/Typography/Heading.svelte"
    import Image from "$lib/kit/Elements/Image.svelte"

    import lock1 from "./lock.svg"
    import lock2 from "./lock2.svg"
    import LabelElement from "$lib/kit/Elements/Atomic/LabelElement.svelte"
    import Columns from "$lib/kit/Stencils/Columns.svelte"
    import Table from "$lib/kit/Tables/Table/index.js"
</script>

<Title title="Сети и соединения"/>

<Section>
    <Table>
        <Table.Row slot="head"><Table.HCell>Длина</Table.HCell><Table.HCell>Количество</Table.HCell><Table.HCell>Перебор</Table.HCell></Table.Row>
        <Table.Row><Table.Cell n>4</Table.Cell><Table.Cell n>1624</Table.Cell><Table.Cell>3 часа</Table.Cell></Table.Row>
        <Table.Row><Table.Cell n>5</Table.Cell><Table.Cell n>7152</Table.Cell><Table.Cell>12 часов</Table.Cell></Table.Row>
        <Table.Row><Table.Cell n>6</Table.Cell><Table.Cell n>26016</Table.Cell><Table.Cell>2 дня</Table.Cell></Table.Row>
        <Table.Row><Table.Cell n>7</Table.Cell><Table.Cell n>72912</Table.Cell><Table.Cell>5 дней</Table.Cell></Table.Row>
        <Table.Row><Table.Cell n>8</Table.Cell><Table.Cell n>140704</Table.Cell><Table.Cell>10 дней</Table.Cell></Table.Row>
        <Table.Row><Table.Cell n>9</Table.Cell><Table.Cell n>140704</Table.Cell><Table.Cell>10 дней</Table.Cell></Table.Row>
        <Table.Row><Table.Cell n>Всего</Table.Cell><Table.Cell n>389112</Table.Cell><Table.Cell>27 дней</Table.Cell></Table.Row>
    </Table>

    <Columns>
        <Image src={lock1} width="16rem" height="16rem" caption="Правши">
            <LabelElement top="15%" left="15%" label="45%"/>
            <LabelElement top="15%" left="50%" label="9%"/>
            <LabelElement top="15%" left="85%" label="13%"/>
            <LabelElement top="50%" left="15%" label="6%"/>
            <LabelElement top="50%" left="50%" label="3%"/>
            <LabelElement top="50%" left="85%" label="2%"/>
            <LabelElement top="85%" left="15%" label="15%"/>
            <LabelElement top="85%" left="50%" label="3%"/>
            <LabelElement top="85%" left="85%" label="4%"/>
        </Image>
        <Image src={lock2} width="16rem" height="16rem" caption="Левши">
            <LabelElement top="15%" left="15%" label="53%"/>
            <LabelElement top="15%" left="50%" label="9%"/>
            <LabelElement top="15%" left="85%" label="9%"/>
            <LabelElement top="50%" left="15%" label="9%"/>
            <LabelElement top="50%" left="50%" label="2%"/>
            <LabelElement top="50%" left="85%" label="1%"/>
            <LabelElement top="85%" left="15%" label="13%"/>
            <LabelElement top="85%" left="50%" label="1%"/>
            <LabelElement top="85%" left="85%" label="4%"/>
        </Image>
    </Columns>
</Section>