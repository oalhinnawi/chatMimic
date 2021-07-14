# Modules:
#     twitchAPI==2.3.2
#     textgenrnn==2.0.0


import twitch
from textgenrnn import textgenrnn


class ChatMimic:

    def _deEmojify(self, inputString):
        """Removes emojis and emoticons from text, returns plaintext"""
        return inputString.encode('ascii', 'ignore').decode('ascii')

    def __init__(self, clientID, clientSecret):

        print("Logging into twitch")
        # Login and initialize
        try:
            self.helix = twitch.Helix(clientID, clientSecret)
            print("Logged in")
        except Exception as e:
            raise(e)

    def trainOnVOD(self,
                   vodID,
                   bufferFile="temp.txt",
                   saveOutWeights=True,
                   weightsOutputFile="vodWeights.hdf5",
                   numEpochs=10):
        """Trains text generator on given VOD ID"""
        print("Scraping VOD for chat history")
        # Get all chat from VOD and put it in a buffer file
        fileObj = open(bufferFile, "w")

        for comment in self.helix.video(vodID).comments:
            text = self._deEmojify(comment.message.body)
            fileObj.write(text + "\n")

        fileObj.close()

        print("Beginning training on VOD Chat")
        # Train text generator on said file
        self.vodGen = textgenrnn()
        self.vodGen.train_from_file(bufferFile, num_epochs=numEpochs)
        # Save out weights if enabled
        if(saveOutWeights):
            print("Saving out weights to {}".format(weightsOutputFile))
            self.vodGen.save(weightsOutputFile)

    def loadVODWeights(self, filePath):
        """Loads HDF5 file representing the weights for generator"""
        try:
            self.vodGen
        except AttributeError:
            print("Generator hasn't been made yet, making now")
            self.vodGen = textgenrnn()
        print("Loading in weights {}".format(filePath))
        self.vodGen.load(filePath)

    def generateTextFromVOD(self):
        """Generates Text based on current weights"""
        if(self.vodGen):
            return self.vodGen.generate(1, return_as_list=True)[0]
        else:
            raise("VOD text generator not trained")
