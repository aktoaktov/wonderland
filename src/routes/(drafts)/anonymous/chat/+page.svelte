<script>
import Title from "$lib/kit/Elements/Title.svelte"
import Table from "$lib/kit/Tables/Table/index.js"
import Code from "$lib/kit/Code/Code.svelte"
import Icon from "$lib/kit/Elements/Icon.svelte"
import Comment from "$lib/kit/Elements/Comment.svelte"
</script>

<Title title="Анонимность"/>

<Table centered>
    <Table.Row slot="head">
        <Table.HCell sticky></Table.HCell>
        <Table.HCell>E2EE</Table.HCell>
        <Table.HCell>FS</Table.HCell>
        <Table.HCell>ZAE</Table.HCell>
        <Table.HCell>Свое<br/>шифрование</Table.HCell>
        <Table.HCell>Защита<br/>метаданных</Table.HCell>
        <Table.HCell>Открытый<br/>код</Table.HCell>
        <Table.HCell>Конфиденциальность</Table.HCell>
        <Table.HCell>Анонимная<br/>регистрация</Table.HCell>
        <Table.HCell>Возможно<br/>через Tor</Table.HCell>
    </Table.Row>


    <Table.Row>
        <Table.Cell sticky>Singal</Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell>Хорошо</Table.Cell>
        <Table.Cell>Телефон</Table.Cell>
        <Table.Cell>Виртуализация</Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Berty</Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell>Хорошо</Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Telegram</Table.Cell>
        <Table.Cell>Частично (только лс)</Table.Cell>
        <Table.Cell>Частично (секретные чаты)</Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="yes"/> (MTProto)</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Частично</Table.Cell>
        <Table.Cell>E2EE выключено по умолчанию</Table.Cell>
        <Table.Cell>Телефон</Table.Cell>
        <Table.Cell>Прокси</Table.Cell>
    </Table.Row>


    <Table.Row>
        <Table.Cell sticky>Snapchat</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Плохо</Table.Cell>
        <Table.Cell><Icon name="no"/> (но возможно)</Table.Cell>
        <Table.Cell>Виртуализация</Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Teams</Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Ужасно</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Виртуализация</Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Discord</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Ужасно</Table.Cell>
        <Table.Cell>Почта</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Viber</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="yes"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Ужасно</Table.Cell>
        <Table.Cell>Почта</Table.Cell>
        <Table.Cell>Виртуализация</Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Skype</Table.Cell>
        <Table.Cell>Частично (только лс)</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Ужасно</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Виртуализация</Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>WeChat</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Ужасно</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>WhatsApp</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell>Ужасно</Table.Cell>
        <Table.Cell>Телефон</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
    </Table.Row>

    <Table.Row>
        <Table.Cell sticky>Zoom</Table.Cell>
        <Table.Cell><Icon color="stroke" name="question"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="question"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
        <Table.Cell><Icon color="stroke" name="minus"/></Table.Cell>
        <Table.Cell>Почта</Table.Cell>
        <Table.Cell><Icon name="no"/></Table.Cell>
    </Table.Row>


</Table>