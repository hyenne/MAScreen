const noble = require('noble');
const zerorpc = require("zerorpc");

var peripheralUUID = 'd16c118703cc'; //'ce7ad00da0ac4463983bd328cb3edeff'; 맥북에서는 이거였음
var characteristicUUID = '6e400002b5a3f393e0a9e50e24dcca9e';
var writer = null;

var server = new zerorpc.Server({
  draw: function(data, reply) {
      draw(data);
      reply(null, "sent");
  }
});

function strToByte(str) {
  var data = Uint8Array.from(Buffer.from(str, 'hex'));
  var tmp = [];
  var i = 0;
  while(true) {
    if (data.length - i < 20) {
      tmp.push(data.slice(i));
      break;
    } else {
      tmp.push(data.slice(i, i + 20));
      i += 20;
    }
  }
  var result = []
  tmp.forEach(a => result.push(new Buffer.from(a)));
  return result;
}

function draw(data) {
  strToByte(data).forEach(b => {
    writer.write(b, false, err => {});
  })
}

noble.on('stateChange', state => {
  if (state === 'poweredOn') {
    noble.startScanning();
  } else {
    noble.stopScanning();
  }
});

noble.on('discover', async peripheral => {
  if (peripheral.uuid == peripheralUUID) {
    noble.stopScanning();
    peripheral.connect(async err => {
      peripheral.discoverAllServicesAndCharacteristics((err, services, characteristics) => {
        characteristics.forEach(async characteristic => {
          if (characteristic.uuid == characteristicUUID) {
            console.log('connected');
            writer = characteristic;
            server.bind("tcp://0.0.0.0:4242");
          }
        })
      });
    })
  }
});
