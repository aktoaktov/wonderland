<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"

    import imageMapAndGraphExample from "./map-and-graph-example.svg"
    import Image from "$lib/Elements/Image.svelte"
    import Fact from "$lib/Stencils/Blocks/Fact.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
</script>

<Title title="Функции и отображения"
/>


<Definition title="Отображение">
    <P>
        Пусть у нас есть два множества <Math m={`X`}/> и <Math m={`Y`}/>.
        Обозначим за <Math m={`f`}/> какое-то правило, по которому каждому элементу из множества <Math m={`X`}/>
        ставится в соответствие какой-то один элемент множества <Math m={`Y`}/>.
        Это правило <Math m={`f`}/> называется <b>функцией</b> или <b>отображением</b> (map).
        Записывается
    </P>
    <Math display m={`f \\colon X \\to Y \\qquad \\text{или} \\qquad X \\xrightarrow{f} Y`}/>

    <P>
        Множество <Math m={`X`}/> называется <b>областью определения</b> функции <Math m={`f`}/>,
        обозначается <Math m={`\\dom f`}/> (domain).
    </P>
    <P>
        Множество <Math m={`Y`}/> называется <b>областью назначения</b> функции <Math m={`f`}/>,
        обозначается <Math m={`\\codom f`}/> (codomain).
    </P>
</Definition>

<Par>
    <P>
        Есть еще один, чуть более фундаментальный и запутанный подход к определению отображений.
        Если элементу <Math m={`x \\in X`}/> ставится в соответствие элемент <Math m={`y \\in Y`}/>,
        то будем интерпретировать это &laquo;соответствие&raquo; как пару <Math m={`(x, y)`}/>.
    </P>
    <P>
        Тогда отображение <Math m={`f \\colon X \\to Y`}/> задается
        просто каким-то подмножеством <Math m={`f \\subset X \\times Y`}/>.
        Это подмножество <Math m={`f`}/> должно удовлетворять свойству функциональности.
        Для любого <Math m={`x \\in X`}/> существует ровно один <Math m={`y \\in Y`}/> такой,
        что <Math m={`(x, y) \\in f`}/>.
    </P>
</Par>

<Fact>
    {#snippet title()}Термин &laquo;область значений&raquo;{/snippet}
    <P>
        В русской литературе есть термин &laquo;область значений&raquo;, значение которого сильно зависит от контекста.
        В каких-то случаях область значений <Math m={`f`}/> значит <Math m={`\\codom f`}/>,
        а в каких-то <Math m={`\\im f`}/>.
    </P>
    <P>
        Во избежание путаницы я буду использовать английские термины codomain of the function и image of the function.
    </P>
    <P>
        Кстати, название &laquo;область назначения&raquo; я выдумал сам.
    </P>
</Fact>


<Definition title="График отображения">
    <P><b>График</b> отображения <Math m={`f \\colon X \\times Y`}/> &mdash; подмножество <Math m={`X \\times Y`}/></P>
    <Math display m={`\\graph f \\defeq \\big\\{ (x, y) \\in X \\times Y \\colon y = f(x) \\big\\}`}/>
</Definition>

<Par>
    <P>
        Вот пример отображения <Math m={`\\{\\text{A}, \\text{B}, \\text{C}\\} \\to \\{1, 2\\}`}/> и его
        график <Math m={`\\big\\{ (\\text{A}, 1), (\\text{B}, 2), (\\text{C}, 1) \\big\\}`}/>
    </P>
    <Image src={imageMapAndGraphExample} alt={`Пример отображения из множества {A, B, C} в множество {1, 2}`}/>
</Par>


<Definition title="Образ множества">
    <P>
        <b>Образ множества</b> <Math m={`A \\subset \\dom f`}/> при отображении <Math m={`f`}/> &mdash; множество
        образов его элементов. Обозначается
    </P>
    <Math display m={`f[A] \\defeq \\big\\{ f(x) \\enspace \\forall x \\in A \\big\\}`}/>
</Definition>

<Par>
    <P>
        Например, если <Math m={`g`}/> &mdash; отображение из предыдущего примера,
        то <Math m={`g\\big[\\{\\text{A}, \\text{C}\\}\\big] = \\{1\\}`}/>.</P>
    <P>
        <b>Область значений</b> отображения <Math m={`f`}/> &mdash; образ области определения <Math m={`f`}/>.
        Обозначается <Math m={`\\rng f \\defeq f\\big[\\dom f\\big]`}/>.
    </P>
</Par>

<Par>
    <P>
        <b>Композиция</b> двух отображений <Math m={`f \\colon X \\to Y`}/> и <Math m={`g \\colon Y \\to Z`}/> &mdash;
        отображение <Math m={`g \\compose f \\colon X \\to Z`}/>, в котором <Math m={`x \\mapsto g\\big(f(x)\\big)`}/>.
        Композиция отображений является ассоциативной операцией, то
        есть <Math m={`(f \\compose g) \\compose h = f \\compose (g \\compose h)`}/>.
    </P>
</Par>


<Subheading>Инъективное отображение</Subheading>

<Par>
    <P>
        Отображение <Math m={`f \\colon X \\to Y`}/> называется <b>инъективным</b> или вложением, если разные
        элементы <Math m={`X`}/> переходят в разные элементы <Math m={`Y`}/>.
        Формально, <Math m={`f(x) = f(y) \\Rightarrow x = y`}/>, или <Math m={`x != y \\Rightarrow f(x) = f(y)`}/>.
        Записывается
    </P>
    <Math display m={`f \\colon X \\injto Y \\qquad \\text{или} \\qquad X \\xinjto{f} Y`}/>
</Par>


<Subheading>Сюръективное отображение</Subheading>

<Par>
    <P>
        Отображение <Math m={`f \\colon X \\to Y`}/> называется <b>сюръективным</b>, если все
        элементы <Math m={`Y`}/> являются образами элементов <Math m={`X`}/>.
        Формально, <Math m={`f[X] = Y`}/> или <Math m={`Y = \\rng f`}/>.
        Записывается
    </P>
    <Math display m={`f \\colon X \\surjto Y \\qquad \\text{или} \\qquad X \\xsurjto{f} Y`}/>
</Par>

<Subheading>Биективное отображение</Subheading>

<Par>
    <P>
        Отображение <Math m={`f \\colon X \\to Y`}/> называется <b>биективным</b>, если оно одновременно и инъективно,
        и сюръективно.
        Такое отображение задает взаимно однозначное соответствие между множествами <Math m={`X`}/> и <Math m={`Y`}/>.
        Записывается
    </P>
    <Math display m={`f \\colon X \\bijto Y \\qquad \\text{или} \\qquad X \\xbijto{f} Y`}/>
    <P>Композиция биекций также является биекцией.</P>
</Par>


<Subheading>Обратные отображения</Subheading>

<Par>
    <P>
        <b>Тождественное отображение</b> <Math m={`\\Id_X`}/> множества <Math m={`X`}/> &mdash; отображение, которое
        каждый элемент переводит в себя.
    </P>
    <Math display m={`\\Id_X \\colon X \\to X ~\\text{где}~ x \\mapsto x`}/>
</Par>
<Par>
    <P>
        <b>Обратное</b> к отображению <Math m={`f \\colon X \\to Y`}/> &mdash;
        отображение <Math m={`f^-1 \\colon Y \\to X`}/> такое,
        что <Math m={`f \\compose f^-1 = \\Id_X`}/> и <Math m={`f^-1 \\compose f = \\Id_Y`}/>.
    </P>
    <P>
        Отображение обратимо тогда и только тогда, когда оно является биекцией. На самом деле можно так же обратить
        и инъективное отображение, но нужно дополнительно изменить область определения обратного.
    </P>
</Par>

