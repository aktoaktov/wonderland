<script>
import Title from "$lib/Elements/Title.svelte"
import Par from "$lib/Markup/Par.svelte"
import P from "$lib/Markup/P.svelte"
import Codeblock from "$lib/Code/Codeblock.svelte"
import Code from "$lib/Code/Code.svelte"
</script>

<Title title="Циклы"
/>

<Par>
    <P>

    </P>
</Par>

<Par>

<P>
    Для бесконечного выполнения куска кода <Code c="..."/> используется конструкция бесконечного цикла
</P>
<Codeblock code={
`forever:
    ...`
}/>
    <P>
        Одно из главных свойств алгоритмов &mdash; конечность.
        Кажется, что смысла в бесконечных циклах нет. Но это не так.
        Бесконечные циклы нужны тогда, когда условий выхода много, и они заранее неизвестны,
        или если в цикле происходит какая-то недетерминированная дичь, при которой выход не определен.
    </P>
    <P>
        Иногда еще бесконечные циклы используют для бесконечных итераторов.
    </P>
    <P>
        Вообще, в нормальных языках программирования нет конструкции <Code c="forever"/>.
        Эту конструкцию можно заменить циклом с условием, которое всегда верно: <Code c="while true"/>.
    </P>
</Par>
