%{
  #include<stdio.h>
%}
%%
stmt:A exp B
    ;
exp :A exp B  {$$=$1 exp $2}
    |B exp A  {$$=$2 exp $1}
    |B exp B  {$$=$2 exp $2}
    |A exp A  {$$=$1 exp $1}
    |A        {$$=$1}
    |B        {$$=$2}
    |         {$$}
    ;
%%
main()
{
  return(yyparse());
}
