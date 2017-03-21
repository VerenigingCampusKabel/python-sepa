from signxml import XMLSigner, XMLVerifier

signer = XMLSigner()
verifier = XMLVerifier()

def sign(tree, key, cert):
    return signer.sign(tree, key=key, cert=cert)

def verify(tree):
    return bool(verifier.verify(tree).signed_xml)
