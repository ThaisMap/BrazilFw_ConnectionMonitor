const Puppeteer = require ('puppeteer');

module.exports = {
    async getActiveConnections() {
        const browser = await Puppeteer.launch({
            args: [
                '--ignore-certificate-errors',
            ],
            headless: true,
            defaultViewport: null,
            ignoreHTTPSErrors: false
        });
        const page = await browser.newPage();
        page.setExtraHTTPHeaders({
            'authorization': 'Basic cm9vdDpiclQxMDEyKg==',
        });
        await page.goto('https://192.168.0.5:8181/connection-monitor.php');    
        // Scrape
        const result = await page.evaluate(() => {
        const conexoes = [];
        const ignorar = [ "127.0.0.1", "192.168.0.2", "192.168.0.5"]
        let contRepetidos = 0;
        document.querySelectorAll('table.listview-1 > tbody > tr').forEach(
            linhas => {
                linha = linhas.querySelectorAll('th');

                    const data = Date();
                    const origem = linha[2].innerText;
                    const destino = linha[3].innerText;
                    const id = origem+destino;
                    if ((conexoes.findIndex(con => con.id == id) == -1) && (!ignorar.includes(origem) && !ignorar.includes(destino)))
                    {            
                        const conexao = { id, data, origem, destino, };
                        conexoes.push(conexao);
                    }
                }
            );
        return conexoes;
        });
        
        browser.close();
        return result
    },
}
