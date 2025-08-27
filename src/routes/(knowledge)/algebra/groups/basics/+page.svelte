<script>
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Title from "$lib/Elements/Title.svelte"
</script>

<Title title="Группы"
/>

<Definition title="Группа">
    <P>
        <b>Группа</b> <Math m="G"/> &mdash; множество <Math m="G"/> с заданной на нём бинарной
        операцией <Math m="G \times G \to G"/>, удовлетворяющей условиям
    </P>
    <EnumList>
        <ListItem>
            ассоциативность: <Math m="a \cdot (b \cdot c) = (a \cdot b) \cdot c"/>
        </ListItem>
        <ListItem>
            существует нейтральный элемент <Math m="1"/>, для которого <Math m="1 \cdot a = a \cdot 1 = a"/>
        </ListItem>
        <ListItem>
            для любого элемента найдется обратный, такой, что
            <Math m="a \cdot a^-1 = 1"/>
        </ListItem>
    </EnumList>
</Definition>

<Par>
    <P>
        <b>Порядок элемента</b> <Math m="\ord a"/> &mdash; наименьшее число <Math m="n"/> такое, что <Math m="a^n = 1"/>.
        Если <Math m="a^n = 1"/>, то <Math m="\ord a \divides n"/>
    </P>
</Par>
      
