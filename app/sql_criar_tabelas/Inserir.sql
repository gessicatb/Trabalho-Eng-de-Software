INSERT INTO "PlataformaDigital" ("CNPJ", "Nome", "ValorPagoReproducao") VALUES
  ('11111111111111', 'Playstation store', 0.00348),
  ('22222222222222', 'Steam', 0.00675),
  ('33333333333333', 'Epic Games', 0.00562),
  ('44444444444444', 'Amazon', 0.01123),
  ('55555555555555', 'Xbox', 0.00022);
 
INSERT INTO "PlataformaDigital" ("CNPJ", "Nome", "ValorPagoReproducao") VALUES
  ('66666666666666', 'Tidal', 0.00876),
  ('77777777777777', 'SoundCloud', 0.00252),
  ('88888888888888', 'Pandora', 0.00203),
  ('99999999999999', 'Google Play Music', 0.00475);

  
 INSERT INTO "GeneroJogo" ("GeneroJogo_PK", "GeneroJogo") VALUES
  (1, 'Ação'),
  (2, 'Puzzle'),
  (3, 'Multiplayer'),
  (4, 'Aventura'),
  (5, 'FPS');

INSERT INTO "GeneroJogo" ("GeneroJogo_PK", "GeneroJogo") VALUES
  (6, 'RPG'),
  (7, 'Indie'),
  (8, 'Estratégia'),
  (9, 'MOBA'),
  (10, 'Corrida');

INSERT INTO "GeneroJogo" ("GeneroJogo_PK", "GeneroJogo") VALUES
  (16, 'Simulação'),
  (17, 'Esportes'),
  (18, 'Terror'),
  (19, 'MMORPG'),
  (20, 'Survival');