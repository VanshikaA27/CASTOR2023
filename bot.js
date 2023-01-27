const Telegraf = require('telegraf')
const bot = new Telegraf(`YOUR_TOKEN_HERE`)
bot.start((ctx) => ctx.reply('Welcome to the appointment scheduling bot! How can I help you today?'))
bot.command('schedule', (ctx) => {
    ctx.reply('What date would you like to schedule your appointment for?')
    // Use conversation middleware to handle user input and continue scheduling process
})
bot.command('cancel', (ctx) => {
    ctx.reply('What date is the appointment you would like to cancel?')
    // Use conversation middleware to handle user input and continue cancelling process
})