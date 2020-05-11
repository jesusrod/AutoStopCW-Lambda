Copyright (c) 2020. Amazon Web Services Ireland LTD. All Rights Reserved.
AWS Enterprise Support Team
Name : AutoStopCW-Lambda
Version : 1.0.0
Encoded : No
Paramaters : None
Platform : Any EC2
Associated Files: None
Abstract : ReadMe Document
Revision History : - 1.0.0 | 07/05/2020 Initial Version
Author : Jesus Rodriguez

##################### Automation Stop and Start.##########################################################################
YOU ACKNOWLEDGE AND AGREE THAT THE SCRIPT IS PROVIDED FREE OF CHARGE "AS IS" AND "AVAILABLE" BASIS, AND THAT YOUR
USE OF RELIANCE UPON THE APPLICATION OR ANY THIRD PARTY CONTENT AND SERVICES ACCESSED THEREBY IS AT YOUR SOLE RISK AND
DISCRETION. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

##########################################################################################################################

# AutoStopCW-Lambda
Lambda Script to Apply CW alarm to Stop an EC2 instance based on tags when the threshold is met.

The purpose of this process is to identify whenever an instance with a particular tag ("AutoStop") is started and it's not being utilised (idle) for a period of time, then the instance will automatically stop.

This Lambda Script makes use of CloudWatch Event pattern to trigger and create CloudWatch Alarms over EC2 resources when they Start - Specifically when their state change to "running" and has a tag attached with the key "AutoStop". The CW Alarm will monitor NetworkOut bytes sent out on all network interfaces by the instance aiming to identify if there's a logged on user via Remote connection. The evaluation period must be configured with the premise of how long the idle window is allowed and the Threshold will be the amount of bytes that a Remote Desktop Connection has in average - during my tests, I found that whenever a completely idle instance with Network out bytes of 0, with a remote connection it will increase to an average of 4kb per minute (by having Detailed Monitoring Enabled).

Pre-Requisites for the Script.

    AWS Account, VPC and Subnets. 
    AWS Permissions: Create AWS Role for Lambda to perform CloudWatch actions over EC2, Attach Role to Lambda.
    Instances that have a tag key: AutoStop
    
Deployment guide:

1) In IAM, create a role and attach policy
2) In Lambda, create a new function - Author from scratch
3) Runtime Python 3.6
4) Under permissions use the existent role recently created.
5) Create function
6) Add a trigger and select CloudWatch Events
7) Create a new rule and provide a new name
8) in the rule type, select Event Pattern
9) Select EC2, and below EC2 instance state-change notification. 
10) Click on Detail
11) Select State and choose running
12) Make sure the Enble Trigger option is selected and click on Add
13) Now click on the lambda function and paste the function shared.
14) Save

Once this is deployed, any instance that has a tag of "AutoStop" and starts (changes state to running) will have an Alarm created that will monitor the NetworkOut traffic during the period you adjust and will stop as soon as the threashold is met.

Once an instance receives the new alarm it will stay in the resource until deleted.


