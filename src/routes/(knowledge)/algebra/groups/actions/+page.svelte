<script>
    import P from "$lib/Markup/P.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Par from "$lib/Markup/Par.svelte"
</script>

<Title title="Действия групп"
/>

<P>
    При этом <Math m="g \compose x \in X"/>, единичный элемент оставляет{" "}
    <Math m="x"/> на месте, т. е. <Math m="1 \compose x = x"/>, и действие
    ассоциативно, т. е.{" "}
    <Math m="g \compose (h \compose x) = (g \dot h) \compose x"/>.
</P>

<Theorem title="Теорема Кэли">
    Любая группа <Math m="G"/> изоморфна какой-то
    подгруппе <Math m="\mathrm S (G)"/>
</Theorem>

<Proof>
    <P>
        Действие <Math m="G \acts G"/> – гомоморфизм{" "}
        <Math m={`G \\overset{\\varphi}{\\longrightarrow} \\mathrm{S}(G)`}/>
        .
    </P>
    <P>
        Гомоморфизм <Math m="\varphi"/> инъективен, то есть если{" "}
        <Math m="g_1 \neq g_2"/>, то{" "}
        <Math m="\varphi(g_1) \neq \varphi(g_2)"/>.
    </P>
    <P>
        Значит, <Math m="G \cong \im \varphi \sub \mathrm S(G)"/>.
    </P>
</Proof>

<Subheading>Эффективность</Subheading>

<Par>
    <P>
        <b>Эффективное действие</b> – действие, при котором каждый элемент
        группы, кроме нейтрального, действует нетождественно.
        (двигаются все элементы)
    </P>
</Par>

<Par>
    <P>
        Пусть <Math m="\alpha = G \acts X"/> – действие группы на множество.
    </P>
    <P>
        <b>Ядро неэффективности</b> действия <Math m="\alpha"/> – множество
        тех элементов группы, которые действуют на элементы множества
        тривиально (оставляют их на месте).
    </P>
    <P>
        Действие <Math m="\alpha"/> эффективно, если{" "}
        <Math m="{`\\ker \\alpha = \\{1\\}`}"/>.
    </P>
    <P>
        Любое действие можно сделать эффективным, отфакторизовав{" "}
        <Math m="G"/> по ядру неэффективности. Теперь действие
        <Math m="G / \ker \alpha \acts X"/> эффективно.
    </P>
</Par>

<Par>
    <P>
        <b>Эквивалентность относительно действия</b> группы <Math m="G"/>{" "}
        элементов множества <Math m="X"/>
    </P>
    <P>
        Если для <Math m="x, y \in X"/> найдется элемент <Math m="g \in G"/>{" "}
        такой, что <Math m="g \compose x = y"/>, тогда <Math m="x \sim y"/>.{" "}
        (<Math m="x"/> и <Math m="y"/> равны с точностью до группы, один
        можно перегнать в другой)

    </P>
</Par>
