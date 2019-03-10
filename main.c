#include <stdio.h>
#include <stdlib.h>

FILE *fp=NULL;
int min=0,max=100,longmin=3,longmax=5;
void getexercise(int n)
{
    int number[20];
    char ioperator[20];
    int worknumber[20],work=1;
    char workoperator[20];
    int ilong=longmin;

    srand((unsigned)time(NULL)+n);
    ilong=rand()%(longmax-longmin+1)+longmin;

    int answer=0,flag=0;

    srand((unsigned)time(NULL)-1+n);
    number[0]=rand()%(max-min+1)+min;
    worknumber[0]=number[0];

    for(int i=0;i<ilong-1;i++)
    {
        srand((unsigned)time(NULL)+i+n);
        flag=rand()%4+1;
        if(flag==1||flag==2)
        {
            if(flag==1)
                ioperator[i]='+';
            else
                ioperator[i]='-';
            workoperator[work-1]=ioperator[i];
            number[i+1]=rand()%(max-min+1)+min;
            worknumber[work]=number[i+1];
        }
        else
        {
            work--;
            number[i+1]=rand()%(max-min+1)+min;
            if(flag==3)
            {
                ioperator[i]='*';
                worknumber[work]=worknumber[work]*number[i+1];
            }
            else
            {
                if(ioperator[i-1]=='/'||ioperator[i-1]=='*')
                {
                    work++;
                    if(i%2==0)
                        ioperator[i]='+';
                    else
                        ioperator[i]='-';
                    workoperator[work-1]=ioperator[i];
                    worknumber[work]=number[i+1];
                }
                else
                {
                    int z;
                    ioperator[i]='/';
                    z=worknumber[work]%number[i+1];
                    worknumber[work]=worknumber[work]-z;
                    number[i]=number[i]-z;
                    worknumber[work]=worknumber[work]/number[i+1];
                }
            }
        }
        work++;
    }
    answer=worknumber[0];
    for(int i=0;i<work-1;i++)
    {
        if(workoperator[i]=='+')
        {
            answer=answer+worknumber[i+1];
        }
        else
        {
            answer=answer-worknumber[i+1];
        }
    }
    fprintf(fp,"%d",number[0]);
    printf("%d",number[0]);
    for(int i=1;i<ilong;i++)
    {
        fputc(ioperator[i-1],fp);
        fprintf(fp,"%d",number[i]);
        printf("%c",ioperator[i-1]);
        printf("%d",number[i]);
    }
    printf("=%d\n",answer);
    fprintf(fp,"=%d\n",answer);
}

void changeMinMax()
{
    printf("Please enter minimum and maximum values:");
    scanf("%d,%d",&min,&max);
}

void changelong()
{
    printf("Please enter Item number range:");
    scanf("%d,%d",&longmin,&longmax);
}
int main()
{
    for(int options=5;options!=0;)
    {
        printf("1:get the exercise\n");
        printf("2:change the Random number range\n");
        printf("3:change the Item number range\n");
        printf("0:EXIT\n");
        printf("Please select options:");
        scanf("%d",&options);
        system("cls");
        if(options==1)
        {
            fp=fopen("exercise.txt","w+");
            fclose(fp);
            fp=fopen("exercise.txt","r+");
            fputs("1753671\n",fp);
            int n=0;
            printf("Please enter the number of expressions:");
            scanf("%d",&n);
            printf("\n");
            printf("1753671\n");
            for(int i=0;i<n;i++)
            {
                getexercise(i*1000);
            }
        }
        if(options==2)
            changeMinMax();
        if(options==3)
            changelong();
        printf("\n\n\n");
    }
    fclose(fp);
    return 0;
}
