create schema shows;
CREATE TABLE shows.quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    source VARCHAR(100) NOT NULL
);

INSERT INTO shows.quotes (quote, source) VALUES
('It''s not who we are underneath, it''s what we do that defines us', 'Batman Begins'),
('You either die a hero or live long enough to see yourself become the villan', 'Batman: The Dark Knight'),
('Freewill is an illusion', 'Supernatural'),
('Miracles do happen dean', 'Supernatural'),
('I''m not great at advice. Can i interest you in a sarcastic comment?', 'Friends'),
('You don''t get to choose who someone wants to be with', 'Lucifer'),
('God has a plan. Yes, but why does everyone think it''s a good plan?', 'Lucifer'),
('I''m daredevil. Not even god can stop that now', 'Daredevil'),
('God feels no pain, all i had to do was become one', 'Flash'),
('Do not go gentle into that good night', 'Interstellar'),
('Love is the one thing we''re capable of perceiving that transcends dimensions of time and space', 'Interstellar'),
('We live in a twilight world and there are no friends at dusk', 'Tenet'),
('Don''t try to understand it. Feel it', 'Tenet'),
('What''s happened, happened. Which is an expression of faith in the mechanics of the world. It''s not an excuse to do nothing', 'Tenet'),
('Don''t you want to take a leap of faith? Or become an old man, filled with regret, waiting to die alone!', 'Inception'),
('I miss you more than I can bear, but we had our time together. I have to let you go.', 'Inception'),
('No more half-measures', 'Breaking Bad'),
('Hope is a good thing. Maybe best of things and no good things ever die.', 'The Shawshank Redemption');