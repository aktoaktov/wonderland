<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    // import Comment from "$lib/Markup/Comment.svelte"
    import Fact from "$lib/Stencils/Blocks/Fact.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
</script>

<Title title="Алгебраические структуры"
/>

<Definition title="Операции на множестве">
    <P>
        Пусть есть какое-то множество <Math m="S"/>.
    </P>
    <P>
        <b><Math m="n"/>-арной операцией</b> на множестве <Math m="S"/> называется отображение
    </P>
    <Math display m="\phi \colon S^n \to S"/>
</Definition>

<Par>
    <P>
        Если операция бинарная, то есть если <Math m="\phi \colon S \times S \to S"/>,
        то обычно <Math m="\phi(a, b)"/> записывают в инфиксной форме как <Math m="a \,\phi\, b"/>.
    </P>
</Par>

<Par>
    <P>
        Например, всем известная бинарная операция <Math m="+"/> на множестве <Math m="\RR"/>.
    </P>
    <P>
        С примерами известных тернарных операций посложнее.
        Но их всегда можно сконструировать. Возьмем, например, операцию <Math m="\RR^3 \to \RR"/>,
        при которой <Math m="(a, b, c) \mapsto a \cdot b - c"/>.
    </P>
    <P>
        Всем программистам известна условная тернарная операция
    </P>
    <Math display m={`a \\mathbin{?} b : c \\defeq \\cases{b & \\if a \\neq 0 \\\\ c & \\otherwise}`}/>
    <P>
        На неявное приведение типа первого аргумента к логическому здесь стоит просто забить.
    </P>
</Par>

<Definition title="Алгебра">
    <P>
        Множество <Math m="S"/> вместе с набором операций <Math
            m={`\\Sigma = \\{\\phi_1, \\phi_2, \\dotsc, \\phi_k\\}`}/>
        называется <b>алгеброй</b>.
    </P>
    <P>
        Здесь <Math m={`\\phi_i \\colon S^{n_i} \\to S`}/> &mdash; <Math m="n_i"/>-арная операция на множестве <Math
            m="S"/>.
    </P>
    <P>
        Множество <Math m="S"/> называется <b>основой</b> или <b>носителем</b> алгебры, кортеж арностей <Math
            m="(n_1, n_2, \dotsc, n_k)"/> называется <b>типом</b> алгебры, а множество операций <Math m="\Sigma"/>
        называется <b>сигнатурой</b> алгебры.
    </P>
</Definition>

<Fact title="Об обозначениях алгебр">
    <P>
        Людям (мне в том числе) лень строго прописывать алгебру, явно указывая носитель и сигнатуру.
        Очень удобно обозначать носитель обычной заглавной буквой, а алгебру этой же буквой, но красивой.
    </P>
    <P>
        Например, <Math m="\AAA"/> &mdash; алгебра с носителем <Math m="A"/>.
        Аналогично, фраза &laquo;алгебра <Math m="A"/>&raquo; означает алгебру с носителем <Math m="A"/>,
        а сигнатура этой алгебры ясна из контекста.
    </P>
    <P>
        Запись <Math m="a \in \AAA"/> означает, что <Math m="a \in A"/>, то есть <Math m="a"/> &mdash; элемент носителя
        алгебры <Math m="\AAA"/>.
    </P>
</Fact>

<Par>
    <P>
        На носителе <Math m="\RR"/> есть алгебра, сигнатура которой состоит из операций
        <Math m="+"/>, <Math m="-"/>, <Math m="\times"/>, <Math m="\div"/>, <Math m="(a, b) \mapsto a^b"/>.
    </P>
    <P>
        Другой пример. Выберем множество <Math m="X"/>.
        На носителе <Math m="2^X"/> можно задать алгебру, сигнатура которой состоит из операций
        <Math m="\union"/>, <Math m="\sect"/>, <Math m="\symdiff"/>, <Math m="a \mapsto X \without a"/>.
        При этом последняя операция дополнения является унарной.
    </P>
</Par>

<Heading>Свойства операций</Heading>

<Par>
    <P>
        Некоторые часто встречаемые свойства операций имеют специальные названия.
    </P>
</Par>

<Definition title="Нейтральные элементы">
    <P>
        Пусть <Math m="(A, \Sigma)"/> &mdash; алгебра
        и <Math m="\circ \colon A \times A \to A"/> &mdash; какая-то бинарная операция.
    </P>

    <P>
        <b>Левым нейтральным</b> элементом называется элемент <Math m="\1_L \in A"/> такой,
        что для любого элемента <Math m="a \in A"/> выполнено
    </P>
    <Math display m="\1_L \circ a = a"/>

    <P>
        <b>Правым нейтральным</b> элементом называется элемент <Math m="\1_R \in A"/> такой,
        что для любого элемента <Math m="a \in A"/> выполнено
    </P>
    <Math display m="a \circ \1_R = a"/>

    <P>
        <b>Нейтральным</b> элементом называется одновременно и правый, и левый нейтральный.
        То есть такой элемент <Math m="\1 \in A"/>, что
        для любого элемента <Math m="a \in A"/> выполнено
    </P>
    <Math display m="\1 \circ a = a \circ \1 = a"/>
</Definition>

<Par>
    <P>
        Для операции умножения на <Math m="\RR"/> нейтральным является элемент <Math m="1"/>, а для сложения <Math
            m="0"/>.
        При возведении в степень есть правый нейтральный элемент <Math m="1"/>, ведь <Math m="a^1 = a"/>, а левого
        нейтрального элемента нет.
    </P>
</Par>

<Par>
    <P>
        Для коммутативных операций нет разницы между правым и левым нейтральным элементом.
    </P>
    <P>
        Если для какой-то операции существует и правый, и левый элемент, то во-первых они совпадают, а во-вторых этот
        нейтральный элемент единственный.
    </P>
    <P>
        Однако, если существуют только правые (или левые) нейтральные элементы, то их может быть сколько угодно.
    </P>
</Par>

<Definition title="Свойства бинарных операций">
    <P>
        Пусть <Math m="(A, \Sigma)"/> &mdash; алгебра.
        Пусть <Math m="a, b, c \in A"/> &mdash; любые элементы носителя алгебры.
    </P>
    <P>
        Бинарная операция <Math m="\circ \colon A \times A \to A"/> может иметь следующие свойства
    </P>

    <BulletList>
        <ListItem>
            <b>Ассоциативность</b>: <Math m="a \circ (b \circ c) = (a \circ b) \circ c"/>
        </ListItem>
        <ListItem>
            <b>Коммутативность</b>: <Math m="a \circ b = b \circ a"/>
        </ListItem>
        <ListItem>
            <b>Идемпотентность</b>: <Math m="a \circ a = a"/>
        </ListItem>
    </BulletList>

    <P>
        Две бинарные операции <Math m="\circ, \diamond \colon A \times A \to A"/> могут обладать следующими свойствами
    </P>

    <EnumList>
        <ListItem>
            <b>Дистрибутивность</b> <Math m="\diamond"/> по <Math m="\circ"/> <b>слева</b>:
            <Math m="a \diamond (b \circ c) = (a \diamond b) \circ (a \diamond c)"/>
        </ListItem>
        <ListItem>
            <b>Дистрибутивность</b> <Math m="\diamond"/> по <Math m="\circ"/> <b>справа</b>:
            <Math m="(b \circ c) \diamond a = (b \diamond a) \circ (c \diamond a)"/>
        </ListItem>
        <ListItem>
            <b>Дистрибутивность</b> <Math m="\diamond"/> по <Math m="\circ"/> &mdash; выполняется и левая, и правая дистрибутивность.
        </ListItem>
    </EnumList>
</Definition>