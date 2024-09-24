from os import listdir

class Utils(object):
    
    @staticmethod
    def load_cogs(cogs_directory: str = "./cogs"):
        """Load all cogs from a directory.

        Args:
            cogs_directory (str, optional): The directory where the cogs are stored. Defaults to "./cogs".

        Returns:
            _type_: A list of cogs.
        """
        cogs = []
        for cogsFile in listdir(cogs_directory):
            if cogsFile.endswith(".py"):
                cogs.append("cogs."+cogsFile[:-3])
                
        return cogs