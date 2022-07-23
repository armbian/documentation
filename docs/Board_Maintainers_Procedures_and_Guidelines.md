<h2>Board Maintainers Procedures and Guidelines</h2>
<p>
	This topic should give you as new board maintainers a brief overview about what you should do, must do, and can do. What you as maintainer can expect from Armbian and what we expect from you.
</p>

<p>
<h2><strong>Requirements:</strong></h2>
</p>

<p>
	Even though you became a maintainer already just to make sure everything is set.
</p>


<ul>
	<li>
		You <strong>must </strong>have access to the hardware you applied to maintain
	</li>
	<li>
		You <strong>must </strong>have a Github ID which should be listed in the <a href="https://docs.armbian.com/Release_Board-Maintainers/" rel="external nofollow">documentation</a>
	</li>
	<li>
		You <strong>must </strong>have a forums account (you already have obviously) which should be listed in the <a href="https://docs.armbian.com/Release_Board-Maintainers/" rel="external nofollow">documentation</a>. If not let me know.
	</li>
    <li>You <strong>must </strong> have an Jira account and keep track of issues filed for your board</li>
        <li> You <strong>must </strong> make sure Armbian Management has been informed of all of the above IDs for our documentation</li>
    <li>
		You <strong>should </strong>know Armbian basics like how to get an Armbian image run on your hardware and do basic debugging, ideally via serial console
	</li>
	<li>
		Knowledge in development, writing code and so on is optional (but of course welcome ;-))
	</li>
</ul>

<i><b>If you are a new maintainer, please make sure you have submitted your IDs and information using our maintainer registry form @ https://www.armbian.com/maintainer-registry/</b></i>

<p>
<h2><strong>Maintaining:</strong></h2>
</p>

<p>
    <b>So all requirements are met and you are a maintainer now. Now what?</b>
</p>

<p>
	Maintainers must not necessarily be persons with development experience. They act as a intersection between end-users and the development team and serve the developers in<em> best-effort</em> manner. They are encouraged to answer basic/simple user questions (if possible, also<em> best effort</em>) without having to bother the development team. They are allowed to record bugs but are not allowed to escalate bugs. Team leaders do.
</p>

<p>
	Take note that it is still up to development team&#39;s discretion what gets attention since Armbian has to plan carefully how to spend its very limited resources.
</p>

<ul>
	<li>
		You <strong>must </strong>participate in release process:<br>
		Ideally you attend to the release meetings that usually happen four times a year about a month before release date (end of February, May, August, November). On that occasion you are given the chance to point out critical issues with your board. A typical agenda looks like this: <a href="https://docs.armbian.com/Process_Release-Model/#agenda" ipsnoembed="true" rel="external nofollow"> https://docs.armbian.com/Process_Release-Model/#agenda</a><br>
		<br>
		However, while the meeting participation is optional you &quot;<strong>must </strong>sign-off that device has been tested, is stable, and ready for release during release process&quot;.
		This basically means you take the <abbr title="Release candidate">RC</abbr>-images we provide and test them as best as you can for their functionality hardware-wise:
        <ul>
            <li>Does the board boot to both CLI and Desktop?</li>
            <li>Is the desktop usable?</li>
            <li>Does USB work? (at all or partially)</li>
            <li>Other common use cases</li>
        </ul><br>
        If something does not work, this is fine also and totally normal. The important part is that it is documented and we get notified about the issues.
        
During each release you will be expected to fill out  the following form: <a href="[https://github.com/EvilOlaf/rc-testing/issues/new?assignees=&amp;labels=for+review&amp;template=form.yml&amp;title=%5BRC%5D%3A+](https://www.armbian.com/rc-testing/)" ipsnoembed="true" rel="external nofollow">Release Testing Form</a>
    </li>
</ul>
<ul>
 <li>
		You <strong>should </strong>follow the <a href="https://github.com/armbian/build/commits/master" rel="external nofollow">commit history</a> on Github. For once you may learn something about how things work both development-wise and behind the scenes in general and also may notice changes that affect the hardware/board you are dealing with. 
	</li>
	<li>
		While not required, you <strong>should </strong>have a <a href="https://docs.armbian.com/Developer-Guide_Build-Preparation/" rel="external nofollow">build environment</a> setup so you can build images with the most recent images and test them right away. Your feedback, either positive or negative, is very welcome. You are free to add comments to every commit and pull request.
        <br>
        <br>
		Ideally you have multiple microSD cards laying around to test regular updates on current releases and nightly without having to re-flash the same card every time to switch between branches.<br><br>
		Alternatively you can grab auto-built images from the build train once available: <a href="https://github.com/armbian/build/releases" rel="external nofollow">https://github.com/armbian/build/releases</a><br><br>
		Take note that the building process takes quite a while so you might be faster using your own build environment.
	</li>
</ul>   
</ul>


<ul>
	<li>
		You <strong>must</strong> provide <em>&quot;best effort&quot;</em> support in the forum:<br>
		Do not let that wording intimidate you. This is not a complicated task. Regarding forums this can include things like
		<ul>
			<li>
				answering obvious questions (for example by pointing to our documentation, ideally directly to the solution page),
			</li>
			<li>
				let the questioner know that additional information is needed for further debugging (e.g. request &quot;armbianmonitor -u&quot; output) or
			</li>
			<li>
				for upgrade issues, ask if they can recreate the issue with a fresh untouched image from: <a href="https://www.armbian.com/download/" ipsnoembed="true" rel="external nofollow">https://www.armbian.com/download/</a>
			</li>
            <li> If you need additional direction on dealing with an issue contact <em>Werner</em> on the forums or Discord.</li>
		</ul>
	</li>
</ul>
<ul>
	<li>
		You <strong>must </strong>provide <em>&quot;best effort&quot;</em> support in Jira:<br>
		<ul>
			<li>
				Review submitted issues for you board made by Armbian's contributors
			</li>
			<li>
				For upgrade issues, ask if they can recreate the issue with a fresh untouched image from: <a href="https://www.armbian.com/download/" ipsnoembed="true" rel="external nofollow">https://www.armbian.com/download/</a>
			</li>
            <li> If you have questions, concerns or are not sure about something, you can tag the issue for <em>@Tenkawa</em> or <em>@TheLinuxBug</em> to review</li>
            		</ul>
	</li>
</ul>

<p>
<h2><strong>Jira and Forum expectations:</strong></h2>
</p>

<strong>Low priority</strong> issues are usually attended to and patched by the community. If the issue has existed for more than a release, you can create a Jira ticket for it. However the expectation is the issue will be low priority and may not be processed for some time. Issues such as, but not limited to, should be considered low priority:
<ul>
    <li>Wifi (this includes missing modules, AP mode, etc)<br></li>
    <li>Bluetooth<br></li>
    <li>GPIO<br></li>
    <li>i2c</li>
    <li>Hardware accelerators, including crypto or VPU (video acceleration)</li>
    <li>DTB overlays (required for i2c devices, LCD displays, etc)</li>
</ul>



For <strong>high priority</strong> items you can create a Jira ticket so that when developers are able, they can process it. If you are going to create a Jira ticket, please be sure to collect as much information about the issue as possible first. If more information will be needed to process the issue, you should reply to the user asking for that additional information and make sure it is included in the ticket. Issues like these should be considered a higher priority:
<ul>
    <li>Image does not boot<br></li>
    <li>Image is corrupt<br></li>
    <li>Packages in the image are corrupt<br></li>
    <li>SDcard or eMMc support is not functioning as expected<br></li>
</ul>


<strong> What should you do if you run into an issue on the forum?</strong>
<ul>
    <li> If the issues is affecting a lot of people, you can create a Jira ticket for the issue to make sure it is reported and seen by developers.</li>
    <li> If you report an issue and you feel it is important, after 8 weeks you can tag (@Tenkawa) in an reply to the ticket and ask for him to review. </li>
    <li> If the issue is important it will be directed to management. If it is deemed not important, you will get a reply stating that we do not have a timeline for the fix and that it will be handled by volunteers when/if possible.</li>
</ul>

<strong>What should you do if there is a long standing Jira ticket?</strong>
<ul>
     <li>If you see an issue and you feel it is important, after 8 weeks you can tag (@Tenkawa) in an reply to the ticket and ask for him to review. </li>
    <li> If the issue is important it will be directed to management, if it is deemed not important, you will get a reply stating that we don't have a timeline for the fix and that it will be handled by volunteers when possible.</li>
</ul>
<p>
<h2><strong>Losing support status:</strong></h2>
</p>
<p>
	As mentioned in the board support rules the support status of a board will be revoked for <strong>at least</strong> the current <strong>and </strong>upcoming release cycle(s) if a &quot;<strong>must</strong>&quot; of the Maintaining section above is not fulfilled.
</p>

<p>
    <b><i>As an example:</i></b> August 30th is release date for 22.08 release, sign-off dead line is 21th. If maintainer misses the <abbr title="Release candidate"><abbr title="Release candidate">RC</abbr></abbr> sign-off window the board is demoted to <abbr title="Community supported Chip - no official support"><abbr title="Community supported Chip - no official support">CSC</abbr></abbr> for both 22.08 and 22.11 releases.
</p>

<p>
	The development team may grant exceptions on their discretion.
</p>

<p>
<h2><strong>Armbian&#39;s assistance:</strong></h2>
</p>

If you have questions about maintainer-ship or want to learn more deeper insights about the build framework and such Armbian will provide you with all information in <em>best-effort</em>. If time allows we can explain and teach you personally various aspects about the project. Otherwise, if  you want to learn more about the build framework, dive in, play with it and <a href="https://docs.armbian.com/Developer-Guide_Build-Preparation/" rel="external nofollow">read the documenenation</a>. Also if you have other concerns please do not hesitate to reach out via forums, IRC or Discord. Armbian cares about the people who care about Armbian&nbsp; <span><img alt=":)" data-emoticon="true" height="20" loading="lazy" src="https://forum.armbian.com/uploads/emoticons/default_smile.png" srcset="https://forum.armbian.com/uploads/emoticons/smile@2x.png 2x" title=":)" width="20"></span>
