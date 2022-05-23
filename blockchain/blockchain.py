import hashlib
import json
import datetime
from flask import Flask, render_template


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {"index": len(self.chain) + 1,
                 "timestamp": str(datetime.datetime.now()),
                 "proof": proof,
                 "previous_hash": previous_hash}
        self.chain.append(block)
        return block

    def print_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:5] == "00000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_proof = previous_block["proof"]
            proof = block["proof"]
            hash_operation = hashlib.sha256(
                str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:5] != "00000":
                return False
            previous_block = block
            block_index += 1
        return True



app = Flask(__name__, template_folder="templates", )
blockchain = Blockchain()


@app.route("/")
def home():
    return render_template("templates.html")


@app.route("/mine_block", methods=["GET"])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {"message": "A block is MINED",
                "index": block["index"],
                "timestamp": block["timestamp"],
                "proof": block["proof"],
                "previous_hash": block["previous_hash"]}
    rsp = StringIO()
    rsp.write(
        """<!doctype html><html><head><link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"></head><body><script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>""")
    rsp.write(json2html.convert(response, table_attributes="class=\"table table-bordered table-hover\""))
    rsp.write(
        '</body><button onclick="goBack()">Go Back</button><script>function"goBack()"{ window.history.back();}</script></html>')
    return rsp.getvalue()


@app.route("/get_chain", methods=["GET"])
def display_chain():
    response = {"chain": blockchain.chain,
                "length": len(blockchain.chain)}
    rsp = StringIO()
    rsp.write(
        """<!doctype html><html><head><link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"></head><body><script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>""")
    rsp.write(json2html.convert(response, table_attributes="class=\"table table-bordered table-hover\""))
    rsp.write(
        '</body><button onclick="goBack()">Go Back</button><script>function"goBack()"{ window.history.back();}</script></html>')
    return rsp.getvalue()


@app.route("/valid", methods=["GET"])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    if valid:
        response = {"message": "The Blockchain is valid."}
    else:
        response = {"message": "The Blockchain is not valid."}
    rsp = StringIO()
    rsp.write(
        """<!doctype html><html><head><link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"></head><body><script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>""")
    rsp.write(json2html.convert(response, table_attributes="class=\"table table-bordered table-hover\""))
    rsp.write(
        '</body><button onclick="goBack()">Go Back</button><script>function goBack() { window.history.back();}</script></html>')
    return rsp.getvalue()


app.run(host="127.0.0.1", port=7777)