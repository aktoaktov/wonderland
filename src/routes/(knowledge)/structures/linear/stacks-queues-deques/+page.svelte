<script>
    import Title from "$lib/Elements/Title.svelte"
    import P from "$lib/Markup/P.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Math from "$lib/Math/Math.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
</script>


<Title title="Стеки, очереди, деки"
/>

<Par>
<P>
    Разберем разновидности линейных списков, в которых доступ к элементам осуществляется только с концов.
</P>
</Par>

<Par>
<P>
    <b>Стек</b> &mdash; линейный список, в котором вставка и удаление выполняются только на одном конце.
</P>
<P>
    <b>Очередь</b> &mdash; линейный список, в котором вставка происходит в один конец, а удаление (извлечение) из
    другого конца.
</P>
<P>
    <b>Дек</b> &mdash; линейный список, в котором доступ, вставка и удаление могут выполняться на обоих концах.
    Дек, получается, может выполнять функции и стека, и очереди.
</P>
</Par>


<Heading>Стек</Heading>

<Par>
<P>
    Элементы в стеке организованы по принципу LIFO (последним вошел &mdash; первым вышел).
</P>
<P>
    Можно представить стек как стопку тарелок: класть новую тарелку можно только на верх стопки и забирать
    тарелки можно только с верху стопки. Из середины тарелки вытаскивать нельзя.
</P>
</Par>

<Heading>Очередь</Heading>

<Par>
<P>
    В очереди элементы организованы по принципу FIFO (первым пошел &mdash; первым вышел).
</P>
<P>
    Очередь, собственно, работает как нормальная человеческая очередь.
    Человек, который раньше в эту очередь встал, раньше из нее выйдет.
</P>
</Par>
