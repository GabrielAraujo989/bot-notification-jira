// importações necessarias para funcionamento do bot
// npm install whatsapp-web.js qrcode-terminal

const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const { exec, spawn } = require('child_process')

// Cliente whatsapp

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {headless:true}

});

// Exibir o QR code

client.on('qr', qr => qrcode.generate(qr, {small:true}));
client.on('read', () => console.log('bot pronto!!!!!'));


// Função para rodar o botJira.py e enviar mensagem para o WhatsApp
function startJiraListener() {
    const python = spawn('python', ['botJira.py']);
    python.stdout.on('data', (data) => {
        const mensagem = data.toString().trim();
        console.log(`[botJira.py] Mensagem bruta recebida: ${data}`);
        if (mensagem) {
            console.log(`[botJira.py] Mensagem processada: ${mensagem}`);

            // Substitua pelo número desejado no formato internacional, ex: '5516993268082@c.us'
            const numero = process.env.WHATSAPP_NUMBER;
            const grupo = process.env.WHATSAPP_GROUP;

            console.log(`[botJira.py] Tentando enviar mensagem para o número: ${numero}`);
            client.sendMessage(numero, mensagem).then(() => {
                console.log(`[botJira.py] Mensagem enviada com sucesso para o número: ${numero}`);
            }).catch(err => {
                console.error(`[botJira.py] Erro ao enviar mensagem para o número: ${err}`);
            });

            console.log(`[botJira.py] Tentando enviar mensagem para o grupo: ${grupo}`);
            client.getChats().then(chats => {
                const chat = chats.find(c => c.isGroup && c.name === grupo);
                if (chat) {
                    client.sendMessage(chat.id._serialized, mensagem).then(() => {
                        console.log(`[botJira.py] Mensagem enviada com sucesso para o grupo: ${grupo}`);
                    }).catch(err => {
                        console.error(`[botJira.py] Erro ao enviar mensagem para o grupo: ${err}`);
                    });
                } else {
                    console.log(`[botJira.py] Grupo '${grupo}' não encontrado. Verifique o nome do grupo no WhatsApp.`);
                }
            }).catch(err => {
                console.error(`[botJira.py] Erro ao buscar grupos: ${err}`);
            });
        }
    });
    python.stderr.on('data', (data) => {
        console.error(`[botJira.py] Erro: ${data}`);
    });
    python.on('close', (code) => {
        console.log(`[botJira.py] Processo finalizado com código ${code}`);
    });
}

// Monitorar eventos de desconexão e reconexão
client.on('disconnected', (reason) => {
    console.error(`[botJira.py] Cliente desconectado. Motivo: ${reason}`);
    console.log('[botJira.py] Tentando reconectar...');
    client.initialize();
});

client.on('ready', () => {
    console.log('bot pronto!!!!!');
    startJiraListener();
});

client.initialize();


//mensagem para 16993268082
