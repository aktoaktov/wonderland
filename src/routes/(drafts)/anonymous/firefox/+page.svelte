<script>
import Title from "$lib/kit/Elements/Title.svelte"
import Table from "$lib/kit/Tables/Table/index.js"
import Code from "$lib/kit/Code/Code.svelte"
</script>

<Title title="Анонимность для в Firefox"/>

<Table>
    <Table.Row>
        <Table.Cell><Code source="geo.enabled"/></Table.Cell>
        <Table.Cell>Включена ли геолокация</Table.Cell>
    </Table.Row>
</Table>