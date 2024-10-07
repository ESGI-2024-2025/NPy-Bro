import os

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
        
        for root, dirs, cogFiles in os.walk(cogs_directory):
            for cogFile in cogFiles:
                if cogFile.endswith(".py"):
                    cogs.append(f"{root[2:].replace('/', '.')}.{cogFile[:-3]}")
                
        return cogs