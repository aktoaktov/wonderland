<script>
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Fact from "$lib/Stencils/Blocks/Fact.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Heading>Бинарные отношения</Heading>

<Par>
    <P>

    </P>
</Par>

<Definition title="Бинарное отношение">
    <P>
        <b>Бинарное отношение</b> <Math m="\diamond"/> из множества <Math m="A"/> в множество <Math m="B"/> &mdash;
        некоторое подмножество <Math m="\diamond \subseteq A \times B"/>.
    </P>
    <P>
        Утверждение <Math m="(a, b) \in \diamond"/> коротко записывается <Math m="a \diamond b"/>.
        Эта запись означает, что элемент <Math m="a \in A"/> находится
        в отношении <Math m="\diamond"/> с элементом <Math m="b \in B"/>.
    </P>
</Definition>

<Par>
    <P>
        Если <Math m="A = B"/>, то есть если <Math m="\diamond \subset A^2"/>, то говорят, что отношение <Math
            m="\diamond"/> является отношением на множестве <Math m="A"/>.
    </P>
</Par>

<Fact title="Инфиксная форма записи">
    <P>Чаще всего отношения записываются в инфиксной форме (это когда знак отношения стоит между операндами)</P>

    <Math display m="a \diamond b \iff (a, b) \in \diamond"/>

    <P>С помощью этой инфиксной формы можно компактно записывать сложные утверждения</P>

    <Math display m="a \diamond b \diamond c \iff a \diamond b \land b \diamond c"/>
</Fact>

<Par>
    <P>
        Есть несколько широкоиспользуемых названий и обозначений для отношения <Math m="\diamond"/> из <Math m="A"/> в
        <Math m="B"/>
    </P>
    <P>
        Множество <Math m="A"/> называется <b>областью отправления</b>, а множество <Math m="B"/> называется <b>областью
        прибытия</b>.
    </P>
    <P>
        Подмножество <Math m="A"/>, каждый элемент которого находится в отношении <Math m="\diamond"/> с каким-то
        элементом из <Math m="B"/> называется <b>областью определения</b> (domain) отношения <Math m="\diamond"/> и
        обозначается
    </P>
    <Math display m={`\\dom (\\diamond) \\defeq \\{ a \\in A : \\exists b \\in B \\; a \\diamond b \\}`}/>

    <P>
        Подмножество <Math m="B"/>, каждый элемент которого участвует в отношении <Math m="\diamond"/> с каким-то
        элементом из <Math m="A"/> называется <b>областью значений</b> (image) отношения <Math m="\diamond"/> и
        обозначается
    </P>
    <Math display m={`\\im (\\diamond) \\defeq \\{ b \\in B : \\exists a \\in A \\; a \\diamond b \\}`}/>
</Par>

<Heading>Действия над отношениями</Heading>

<Par>
    <P>
        Отношения являются множествами, поэтому для них работают обычные множественные операции.
        Итак, для двух отношений <Math m="\alpha \subset A \times B"/> и <Math m="\beta \subset A \times B"/>
        с совпадающими областями отправления и прибытия можно определить
    </P>
    <EnumList>
        <ListItem>
            объединение <Math m="\alpha \union \beta"/>
        </ListItem>
        <ListItem>
            пересечение <Math m="\alpha \sect \beta"/>
        </ListItem>
        <ListItem>
            разность <Math m="\alpha \without \beta"/>
        </ListItem>
    </EnumList>
    <P>
        Также для одного отношения <Math m="\alpha \subset A \times B"/> можно определить дополнение до универсального
        отношения
    </P>
    <Math display m="\alpha^\complement \defeq (A \times B) \without \alpha"/>
</Par>

<Definition title="Обратное отношение">
    <P>
        Пусть <Math m="\alpha"/> &mdash; бинарное отношение из <Math m="A"/> в <Math m="B"/>.
    </P>
    <P>
        <b>Обратное отношение</b> к <Math m="\alpha"/> &mdash; отношение <Math m="\alpha^-1"/> из <Math m="B"/> в <Math
            m="A"/>
    </P>
    <Math display m={`\\alpha^-1 = \\{(b, a) \\in B \\times A : a \\diamond b\\}`}/>

    <P>
        Другими словами, <Math m="b \, \alpha^-1 \, a"/> тогда и только тогда, когда <Math m="a \, \alpha \, b"/>
    </P>
</Definition>

<Par>
    <P>
        Когда мы ищем обратное, мы как бы &laquo;разворачиваем&raquo; отношение.
        Так, например, для отношения <Math m="<"/> на <Math m="\RR"/> обратным является <Math m=">"/>,
        а для отношения равенства обратное оно само.
    </P>
</Par>

<Par>
    <P>Обратным отношением к обратному является исходное</P>
    <Math display m="(\alpha^-1)^-1 = \alpha"/>
</Par>

<Par>
    <P>
        Для множеств <Math m="A"/> и <Math m="B"/> можно задать универсальное отношение <Math m="U"/> из <Math m="A"/> в
        <Math m="B"/>. Это отношение будет состоять из всех пар <Math m="(a, b) \in A \times B"/>.
    </P>
</Par>

<Par>
    <P>
        Бинарное отношение <Math m="\diamond"/> на множестве <Math m="X"/> можно рисовать в виде псевдоорграфа.
    </P>
    <P>
        Множество вершин графа в данном случае совпадает с <Math m="X"/>, а ребро <Math m="uv"/> проводится только
        тогда, когда <Math m="u \diamond v"/>, то есть когда <Math m="a"/> находится в отношении <Math m="\diamond"/> с
        <Math m="b"/>.
    </P>
    <Math display m={`G = \\big( X, \\{ (u, v) \\in V^2 : u \\diamond v \\} \\big)`}/>
</Par>


<Heading>Композиция отношений</Heading>

<Definition title="Композиция отношений">
    <P>
        Пусть <Math m="\alpha \subset A \times B"/> и
        <Math m="\beta \subset B \times C"/> &mdash; два отношения.
        Их <b>композицией</b> называется отношение
    </P>
    <Math display
          m={`\\alpha \\compose \\beta \\defeq \\big\\{ (a, c) \\in A \\times C : \\exists b \\in B \\? a \\,\\alpha\\, b \\land b \\,\\beta\\, c \\big\\}`}/>
    <P>
        Другими словами, <Math m="a \,(\alpha\compose\beta)\, c"/> тогда и только тогда, когда существует
        такое <Math m="b \in B"/>, что <Math m="a \,\alpha\, b"/> и <Math m="b \,\beta\, c"/>.
    </P>
</Definition>

<Par>
    <P>
        Например, на множестве <Math m="\RR"/> композицией отношений <Math m=">"/> и <Math m="\ge"/> является отношение
        <Math m="(>) \compose (\ge) = (>)"/>.
    </P>
</Par>

<Par>
    <P>
        Композиция отношений <Math m="\alpha"/> и <Math m="\beta"/> на одном множестве <Math m="X"/>,
        в общем случае, не коммутативна
    </P>
    <Math display m="\alpha \compose \beta \neq \beta \compose \alpha"/>
</Par>

<Par>
    <P>
        Композиция отношений ассоциативна.
        Для трех отношений <Math m="\alpha \subset A \times B"/>, <Math m="\beta \subset B \times C"/>
        и <Math m="\gamma \subset C \times D"/>
    </P>
    <Math display m="\alpha \compose (\beta \compose \gamma) = (\alpha \compose \beta) \compose \gamma"/>
</Par>

<Par>
    <P>Обратное к произведению отношений является произведение обратных</P>
    <Math display m="(\alpha \compose \beta)^-1 = \beta^-1 \compose \alpha^-1"/>
</Par>

<Subheading>Степень отношения</Subheading>

<Definition title="Степень отношения">
    <P>
        <b>Степенью</b> отношения <Math m="\alpha"/> на множестве <Math m="X"/> называется отношение
    </P>
    <Math display
          m={`\\alpha^n \\defeq \\underbrace{\\alpha \\compose \\alpha \\compose \\dotsb \\compose \\alpha}_{n ~\\text{раз}} `}/>
</Definition>

<Par>
    <P>
        Отсюда <Math m="\alpha^0 = I"/>, <Math m="\alpha^1 = \alpha"/> и <Math m="\alpha^2 = \alpha \compose \alpha"/>.
        А вообще, из ассоциативности следует, что <Math m={`\\alpha^{n} = \\alpha^{n-1} \\compose \\alpha`}/>.
    </P>
</Par>

<Theorem title="Теорема о маленькой степени">
    <P>
        Пусть на множестве <Math m="X"/> из <Math m="n"/> элементов задано отношение <Math m="\alpha \subset X^2"/>.
    </P>
    <P>
        Если какая-то пара <Math m="(x, y)"/> принадлежит какой-то степени отношения <Math m="\alpha^k"/>,
        то эта же пара принадлежит и степени этого отношения не выше <Math m="n-1"/>.
    </P>
    <Math display m="\exists k \? x \, \alpha^k \, y \implies \exists m < n \? x \, \alpha^m \, y"/>
</Theorem>

<Par>
    <P>
        Отсюда можно получить полезный факт.
        Пусть на множестве <Math m="X"/> из <Math m="n"/> элементов задано отношение <Math m="\alpha \subset X^2"/>.
        Тогда
    </P>
    <Math display m={`\\bigunion_{i=1}^\\oo \\alpha^i = \\bigunion_{i=1}^{n-1} \\alpha^i`}/>
</Par>


<Heading>Свойства отношений</Heading>

<Par>
    <P>
        Пусть отношение <Math m="\diamond"/> задано на множестве <Math m="X"/>.
    </P>
</Par>

<Definition title="Рефлексивность">
    <P>
        <b>Рефлексивность</b> &mdash; <Math m="x \diamond x"/> для любых <Math m="x"/>,
        то есть каждый элемент находится в отношении <Math m="\diamond"/> с собой.
    </P>
    <P>
        <b>Антирефлексивность</b> &mdash; <Math m="x \notdiamond x"/>, то есть
        никакой элемент не находится в отношении <Math m="\diamond"/> с собой.
    </P>
</Definition>

<Par>
    <P>
        Например, равенство по модулю чисел из <Math m="\ZZ"/> является рефлексивным отношением.
    </P>
    <P>
        Любое отношение <Math m="\alpha"/> на множестве <Math m="X"/> можно сделать рефлексивным, добавив к нему
        отношение <Math m="\nabla_X"/>.
        Получившееся отношение <Math m="\alpha \union \nabla_X"/> называется <b>рефлексивным замыканием</b> отношения
        <Math m="\alpha"/> и обозначается <Math m="\alpha^r"/>.
    </P>
    <P>
        Также, любое отношение <Math m="\beta"/> на множестве <Math m="X"/> можно сделать антирефлексивным, убрав из
        него отношение <Math m="\nabla_X"/>.
        Получившееся отношение <Math m="\beta \without \nabla_X"/> не носит какого-то особого названия, но иногда бывает
        полезным.
    </P>
</Par>

<Definition title="Симметричность">
    <P>
        <b>Симметричность</b> &mdash; <Math m={`a \\diamond b \\Harr b \\diamond a`}/>.
    </P>
    <P>
        Симметричность отношения на псевдоорграфе означает, что между любыми двумя вершинами проведены ребра в обе
        стороны, а матрица смежности симметрична относительно главной диагонали.
    </P>
    <P>
        <b>Антисимметричность</b> &mdash; <Math m={`a \\diamond b ~\\text{и}~ b \\diamond a \\Rarr a = b`}/>.
    </P>
</Definition>

<Definition title="Транзитивность">
    <P>
        <b>Транзитивность</b> &mdash; <Math m={`a \\diamond b ~\\text{и}~ b \\diamond c \\Rarr a \\diamond c`}/>
    </P>
    <P>
        <b>Нетранзитивность</b> &mdash; существуют такие <Math m="a, b, c"/>, что <Math
            m={`a \\diamond b ~\\text{и}~ b \\diamond c \\,\\nRightarrow\\, a \\diamond c`}/>
    </P>
</Definition>


<Heading>Транзитивное замыкание</Heading>

<Par>
    <P>
        Пусть у нас есть какое-то отношение <Math m="\alpha"/> на <Math m="X"/>.
        Нам хочется построить
    </P>
</Par>