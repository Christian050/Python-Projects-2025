import ezgmail

# Two objects used in code are GmailThread and GmailMessage
# GmailThread represents conversation threads
# GmailMessage represents individual emails within Threads
    
def attatchmentdownload(resultthreads):
    countofresults = len(resultthreads)
    try:
        for i in range(countofresults):
                # checks whether the count of messages in threads is greater than 1
                if len(resultthreads[i].messages) > 1:
                    for j in range(len(resultthreads[i].messages)):
                        resultthreads[i].messages[j].downloadAllAttatchments() # Downloads attatchments for individual messages
                else:
                    # Downloads attatchment(s) for single message
                    resultthreads[i].messages[0].downloadAllAttatchments
                    print("Download Complete. Please check your root directory")
    except:
        raise Exception("Error occurred while downloading attatchment(s).")
    
    if __name__ == "__main__":
        query = input("Enter search query: ")
        # Appending to make sure the result threads always has an attatchment
        newquery = query + "+ has:attatchment"
        # search functions accepts all the operators described at https://support.google.com/mail/answer/7190?hl=en 
        resulthreads = ezgmail.search(newquery)
        if len(resulthreads) == 0:
            # Executed if results don't have attatchment
            print("Result has no attatchments:")
        else:
            print("Result(s) with attatchments:")
            for threads in resulthreads:
                # prints the subject line of email thread in results
                print(f"Email Subject: {threads.messages[0].subject}")
                try:
                    ask = input("Do you want ot download attatchment(s) in result(s) (Yes/No)?") # Allows users to decide whether they want to download attatchment(s) or not.
                    if ask == "Yes":
                        # Calls the function that downloads attatchment(s)
                        attatchmentdownload(resultthreads)
                    else:
                        print("Program exited")
                except:
                    print("Something went wrong")