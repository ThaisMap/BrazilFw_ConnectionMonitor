const Scraper = require('./scrape');

var activeConnections = [];
var closedConnections = [];

async function teste()
{    
    const oldList = activeConnections.map(function(x) {
        return x;
      });
    activeConnections = await Scraper.getActiveConnections();
    getClosed(oldList);
}

function getClosed(oldList){ //in old but not in new
    
    oldList.forEach(element => {
        if(activeConnections.findIndex(con => con.id == element.id) == -1){
            closedConnections.push(element);
        }
    });

    console.log(`Tamanho de ativos: ${activeConnections.length}`);
    console.log(`Tamanho de fechados: ${closedConnections.length}`);
    console.log(closedConnections);
}

teste();
teste();
teste();
teste();
teste();
