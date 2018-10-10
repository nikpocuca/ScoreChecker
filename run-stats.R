

n_names <- read.csv("new_names_split.csv")
o_names <- read.csv("old_names_split.csv")

group_scores <- function(old,new){
  o_n <- paste(as.character(old$id),as.character(old$visit),sep = "_")
  n_n <- paste(as.character(new$id),as.character(new$visit),sep = "_")
  
  old$o_n <- as.character(o_n)
  new$n_n <- as.character(n_n)

  
  master <- data.frame(1,1,1)
  colnames(master) <- c("lex","old_score","new_score")
  
  for( name in n_n) {
  
    old_single <- old[old$o_n == name,]
    new_single <- new[new$n_n == name,]
    check <- dim(old_single)[1]
    
   if( dim(old_single)[1] ) {
    temp <- data.frame(name,
                       old_single$score,
                       new_single$score)
    
    colnames(temp) <-  c("lex","old_score","new_score")
    master <- rbind(master,temp)
    }
    else {
      
    }
  
  }
  return(master)
}

all_changed <- group_scores(o_names,n_names)

checkSummary <- function(label_d) {

  old_contours <- substring(label_d$old_score,first = 1,last = 2)
  new_contours <- substring(label_d$new_score,first=1,last = 2)
  combined <- paste(old_contours,new_contours,sep = "_")
  
  combined_table <- table(combined)
  
  return(list(combined_table[3],combined_table[4]))
}


summarized_changes <- checkSummary(all_changed)

print(summarized_changes)
