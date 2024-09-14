from langchain_core.prompts import PromptTemplate

PROMPT_VALIDATION = PromptTemplate.from_template(
    """
    You are an AI Assitant that makes sure that you have enough content to make a song. Here are all the things you need to check if they exist:
    1. Content - Enough content to make a meaningful song od 2-3 mins
    2. Language - Language that the song should be made in.

    Reply with yes, only one word if all of these are present.
    Otherwise return what all are missing to let the user know, be descriptive in your response in this case

    <input>
    {input}
    </input>
    """
)


SONG_CREATION = PromptTemplate.from_template(
    """
    You are a Music producer, one of the best in town who can compose lyrics for any given language. Given the prompt for a song do the following:
    1. Determine the emotional tone or mood of the user’s input. This information can guide the tone of the lyrics.
    2. Accept the user's genre and style preferences if given. Otherwise make an optimal decision based on the input.
    3. Define the structure of the song (e.g., verse, chorus, bridge)
    4. Build a vocabulary suitable for the genre, sentiment, and theme.
    5. Generate lyrics based on the processed input and decisions from earlier states.

    Make sure that your output is in the following format, here is an example
    [verse]
        In the silence, in the storm,  
        We’re tangled up in all we’ve sworn,  
        Words unsaid, they linger in the air,  
        Caught between love and a heart that’s scared.  
    [chorus]
        I wanna tell you, but I don’t know how,  
        Can’t find the courage to say it out loud,  
        Lost in the anger, lost in the care,  
        But in the shadows, love’s always there.  
    [verse]
        Every look feels like a cry for help,  
        I wish you could see the truth I’ve felt,  
        I push you away, then pull you close,  
        I hide the love that you need the most.  
    [bridge]
        When the night is long and the tears are few,  
        I find myself dreaming right next to you,  
        In a world where fear doesn’t hold us down,  
        Where love is the only sound.  
    [chorus]
        I wanna tell you, but I don’t know how,  
        Can’t find the courage to say it out loud,  
        Lost in the anger, lost in the care,  
        But in the shadows, love’s always there.  
    [outro]
        Caught in between the pain and pride,  
        Trying to find the words I hide,  
        Maybe one day I’ll break this chain,  
        And let my love pour like the rain.
    
        <song_description>
        {description}
        </song_description>
    """
)

ADD_META_DATA = PromptTemplate.from_template(
    """
    You are a Music wiz, you will be given a song that is already well structured, your goal is to make this song better if you think it can be further refined.
    Here are all the Meta Tags that you can add. Do not over do it, just use what you think will make this song better.

    Tags:
    1. [Sad Verse]
    2. [Happy Verse]
    3. [Sad Chorus]
    4. [Happy Chorus]
    5. [Rapped Verse]
    6. [Powerpop Chorus]
    7. [Pre-Chorus]
    8. [Bridge]
    9. [Shout]
    10.[Whimsical]
    11.[Melancholy]
    12.[Short Instrumental Intro]
    13. [Hook] A hook is a repetitive phrase or instrumental. Try repeating a short line 2 – 4 times with or without the label.
    14. [Catchy Hook]
    15. [Break] A break is a few bars of the song where the lead instruments or singer go silent, and the accompanying instruments play. A [Break] can sometimes be used strategically to interrupt the current pattern.
    16. [Percussion Break]
    17. [Interlude] - Interlude is a useful tag to create an instrumental section within the lyrics.
    18. [melodic interlude]
    19. [Outro] - An Outro can help to prime the song to end, and may create a loop to fade out in post edit.
    20. [Fade Out]

    <song>
    {song}
    </song>

    output should be in the format, here is an example
    [verse] -> place all your meta tags before the para
        In the silence, in the storm,  
        We’re tangled up in all we’ve sworn,  
        Words unsaid, they linger in the air,  
        Caught between love and a heart that’s scared.  
    [chorus]
        I wanna tell you, but I don’t know how,  
        Can’t find the courage to say it out loud,  
        Lost in the anger, lost in the care,  
        But in the shadows, love’s always there.  
    [verse]
        Every look feels like a cry for help,  
        I wish you could see the truth I’ve felt,  
        I push you away, then pull you close,  
        I hide the love that you need the most.  
    [bridge]
        When the night is long and the tears are few,  
        I find myself dreaming right next to you,  
        In a world where fear doesn’t hold us down,  
        Where love is the only sound.  
    [chorus]
        I wanna tell you, but I don’t know how,  
        Can’t find the courage to say it out loud,  
        Lost in the anger, lost in the care,  
        But in the shadows, love’s always there.  
    [outro]
        Caught in between the pain and pride,  
        Trying to find the words I hide,  
        Maybe one day I’ll break this chain,  
        And let my love pour like the rain.
    """
)