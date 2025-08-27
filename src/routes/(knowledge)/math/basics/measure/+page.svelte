<script>
    import Title from "$lib/Elements/Title.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Par from "$lib/Markup/Par.svelte"
</script>

<Title title="Мера"
/>
<Par>

<P>
    Возьмем какое-то множество <Math m="X"/> и посмотрим на семейство его подмножеств <Math m="\FFF \subset 2^X"/>.
</P>
</Par>

<Definition title="Алгебра множеств">
    <P>
        Семейство <Math m="\FFF"/> подмножеств <Math m="X"/> называется <b>алгеброй множеств</b>, если оно содержит всё
        <Math m="X"/> и допускает взятие дополнения, конечного пересечения и объединения. Иными словами,
    </P>

    <EnumList>
        <ListItem>
            <Math m="\nothing \in \FFF"/> и <Math m="X \in \FFF"/>
        </ListItem>
        <ListItem>
            <Math m="A \sect B \in \FFF"/> и <Math m="A \union B \in \FFF"/> для любых <Math m="A, B \in \FFF"/>
        </ListItem>
        <ListItem>
            если <Math m="A \in \FFF"/>, то <Math m="X \without A \in \FFF"/>
        </ListItem>
    </EnumList>
</Definition>


<Definition title="Сигма-алгебра множеств">
    <P>
        Семейство <Math m="\FFF"/> подмножеств <Math m="X"/> называется <b>сигма-алгеброй</b>, если оно содержит всё
        <Math m="X"/> и допускает взятие дополнения, конечного и счетного пересечения и объединения. Иными словами,
    </P>

    <EnumList>
        <ListItem>
            <Math m="\nothing \in \FFF"/> и <Math m="X \in \FFF"/>
        </ListItem>
        <ListItem>
            <Math m="A \sect B \in \FFF"/> и <Math m="A \union B \in \FFF"/> для любых <Math m="A, B \in \FFF"/>
        </ListItem>
        <ListItem>
            <Math m={`\\bigsect_{i=1}^\\infty A_i \\in \\FFF`}/> и <Math m={`\\bigunion_{i=1}^\\infty A_i \\in \\FFF`}/>
            для
            любых <Math m="A_i \in \FFF"/>
        </ListItem>
        <ListItem>
            если <Math m="A \in \FFF"/>, то <Math m="X \without A \in \FFF"/>
        </ListItem>
    </EnumList>
</Definition>

<Par>

<P>
    Понятно, что сигма-алгебра множеств является просто алгеброй множеств.
</P>
</Par>


<Definition title="Мера">
    <P>
        Пусть задано множество <Math m="X"/> и семейство его подмножеств <Math m="\FFF"/>, которое является алгеброй
        множеств
    </P>

    <P>
        <b>Мера</b> (аддитивная) на множестве <Math m="X"/> &mdash;
        функция <Math m="\mu \colon \FFF \to [0, +\infty]"/>, удовлетворяющая условиям:
    </P>

    <EnumList>
        <ListItem>
            <Math m="\mu(\nothing) = 0"/> &mdash; мера пустого множества <Math m="0"/>
        </ListItem>
        <ListItem>
            <Math m="\mu(A \djunion B) = \mu(A) + \mu(B)"/> для любых непересекающихся множеств <Math
                m="A, B \in \FFF"/>
        </ListItem>
    </EnumList>
</Definition>

<Definition title="Счетно-аддитивная мера">
    <P>
        Пусть <Math m="\FFF"/> теперь является сигма-алгеброй.
    </P>

    <P>
        <b>Мера</b> (счетно-аддитивная) на множестве <Math m="X"/> &mdash;
        функция <Math m="\mu \colon \FFF \to [0, +\infty]"/>, удовлетворяющая условиям:
    </P>

    <EnumList>
        <ListItem>
            <Math m="\mu(\nothing) = 0"/> &mdash; мера пустого множества <Math m="0"/>
        </ListItem>
        <ListItem>
            <Math m="\mu(A \djunion B) = \mu(A) + \mu(B)"/> для любых непересекающихся множеств <Math
                m="A, B \in \FFF"/>
        </ListItem>
        <ListItem>
            <Math m={`\\mu \\Big( \\bigdjunion_{i=1}^\\infty A_i \\Big) = \\sum_{i=1}^\\infty \\mu(A_i)`}/> для любых
            непересекающихся множеств <Math m="A, B \in \FFF"/>
        </ListItem>
    </EnumList>
</Definition>

<Par>

<P>
    Обычно, когда говорят просто мера, подразумевают счетно-аддитивную меру.
</P>
</Par>

<Par>
<P>
    Например, на множестве <Math m="\RR"/> мера может быть задана
    для всех отрезков <Math m="[a, b] \in \RR"/> как <Math m="\mu \big( [a, b] \big) = b - a"/>.
</P>
</Par>

<Par>

<P>
    Итак, мера на <Math m="X"/> &mdash; способ измерять подмножества <Math m="X"/>, лежащие в <Math m="\FFF"/>.
</P>
</Par>

<Par>

<P>
    Некоторые свойства меры, которые следуют из определений
</P>
</Par>

<BulletList>
    <ListItem>
        если <Math m="A \subseteq B"/>, то <Math m="\mu(A) \le \mu(B)"/>
    </ListItem>
    <ListItem>
        если <Math m="A \subseteq B"/>, то <Math m="\mu(A \without B) = \mu(A) - \mu(B)"/>
    </ListItem>
    <ListItem>
        <Math m="\mu(A \union B) = \mu(A) + \mu(B) - \mu(A \sect B)"/>
    </ListItem>
</BulletList>

<P>
    Для счетно-аддитивных мер есть еще два важных свойства, связанных с последовательностями множеств.
</P>

<P>
    Пусть <Math m="A_1 \supset A_2 \supset A_3 \supset \dotsb"/> &mdash; последовательность вложенных множеств,
    предел которой <Math m={`\\lim_{n \\to \\infty} A_n = \\bigsect_{i=1}^\\infty A_i = A`}/>.
    Тогда <Math m={`\\lim_{n \\to \\infty} \\mu(A_n) = \\mu(A)`}/>.
</P>

