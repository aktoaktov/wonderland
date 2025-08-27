<script>
    import Title from "$lib/kit/Elements/Title.svelte"
    import Hr from "$lib/kit/Elements/Hr.svelte"
    import Contents from "$lib/kit/Layout/Contents.svelte"
    import EnumList from "$lib/kit/Lists/EnumList.svelte"
    import Item from "$lib/kit/Lists/Item.svelte"
    import Link from "$lib/kit/Elements/Link.svelte"
    import UnionInjection from "./UnionInjection.svelte"
    import BasicInjection from "./BasicInjection.svelte"
    import DropInjection from "./DropInjection.svelte"
    import Drop2Injection from "./Drop2Injection.svelte"
</script>


<Title title="SQL инъекции"/>

<Contents>
    <EnumList>
        <Item>
            <Link colorless to="#1">Базовая инъекция</Link>
        </Item>
    </EnumList>
</Contents>

<BasicInjection/>
<Hr/>
<UnionInjection/>
<Hr/>
<DropInjection/>
<Hr/>
<Drop2Injection/>

<br><br><br><br><br>