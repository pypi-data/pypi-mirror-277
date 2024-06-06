from dataclasses import dataclass

def loadDocs():
    try:
        import RTS_DocsBuilder
    except ImportError:
        print("Could not load Documentations, due to missing module.")


    
    try:
        from RTS_DocsBuilder.RInitiate import RInitiate
        initDocs = RInitiate()
        docMemory.initDocs = initDocs
        #print("starting documentation initiator...")
        #print("----------------------------------------------")
        #print(initDocs.topics, initDocs.subtopics)
        #print("Documentations loaded successfully.")
        #print("----------------------------------------------")
        initDocs.execute_initiator()
        

    except ImportError as e:
        print("Could not load modules, due to missing module. Error: ", e)
        return

@dataclass
class CdocMemory():
    initDocs = None

docMemory = CdocMemory()
