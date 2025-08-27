<script>
import Title from "$lib/Elements/Title.svelte"
import Par from "$lib/Markup/Par.svelte"
import P from "$lib/Markup/P.svelte"
import Statement from "$lib/Stencils/Blocks/Statement.svelte"
import Math from "$lib/Math/Math.svelte"
import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Метод центров тяжести"
/>

<Par>
    <P>
        Применим идею метода бинарного поиска (дихотомии)
    </P>
</Par>

<Theorem title="Теорема Грюнбаума–Хаммера–Митягина">

</Theorem>

<Statement>
    <P>
        Пусть <Math m="Q \in \RR^n"/> &mdash; маломерное выпуклое множество (область поиска) и <Math m="f \colon Q \to \RR"/>.
        Решаем задачу
    </P>
    <Math display m={`\\min_{x \\in Q} f(x)`}/>
</Statement>