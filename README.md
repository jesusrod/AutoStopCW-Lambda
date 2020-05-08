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

##################### Automation SQL Deployment.##########################################################################
YOU ACKNOWLEDGE AND AGREE THAT THE SCRIPT IS PROVIDED FREE OF CHARGE "AS IS" AND "AVAILABLE" BASIS, AND THAT YOUR
USE OF RELIANCE UPON THE APPLICATION OR ANY THIRD PARTY CONTENT AND SERVICES ACCESSED THEREBY IS AT YOUR SOLE RISK AND
DISCRETION. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

##########################################################################################################################

# AutoStopCW-Lambda
Lambda Script to Apply CW alarms to EC2 resources based on tags.

The purpose of this process is to identify whenever an instance is started and it's not being utilised (idle) for a period of time, then the instance will automatically stop.

This Lambda Script makes use of CloudWatch Event pattern to trigger and create CloudWatch Alarms over EC2 resources when they Start - Specifically when their state change to "running". The CW Alarm will monitor NetworkOut bytes sent out on all network interfaces by the instance aiming to identify if there's a logged on user via Remote connection. The evaluation period must be configured with the premise of how long the idle window is allowed and the Threshold will be the amount of bytes that a Remote Desktop Connection has in average - during my tests, I found that whenever a completely idle instance with Network out bytes of 0, with a remote connection it will increase to an average of 4kb per minute (by having Detailed Monitoring Enabled).

Pre-Requisites for the Script.

    AWS Account, VPC and Subnets. It is recommended to deploy all EC2 instances into different availability zones for high availability.
    AWS Permissions: Create AWS Role for Lambda to perform actions over EC2, Attach Role to Lambda.


