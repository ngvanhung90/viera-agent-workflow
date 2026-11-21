# Chuyển luật đang áp dụng và tiếp tục công việc

**Gói 3.0.2 — 22/11/2026. Quy trình thi hành một lần tại đúng dự án.**

Tệp này hướng dẫn migration đã được Owner giao, không chứng minh đã cài và không là doctrine sản phẩm thứ hai. Dùng cùng `LENH_AP_DUNG.txt`, luật mới và năm điểm gọi trong `.agents/skills/`.

## 1. Kết quả phải đạt

- Chuẩn bị đúng các nguồn và điều khoản được chỉ định trong task. Chuyển nguồn, cập nhật binding và cho đúng predecessor nghỉ hưu khi riêng tác động đó đã được giao và đạt các cổng tương ứng.
- Giữ kiến trúc, thành tựu, quyền, dữ liệu, công việc dở, identity, lineage, chi phí và bằng chứng cần bảo toàn.
- Có một nguồn có thẩm quyền cho mỗi chủ đề. Giữ nghĩa vụ còn hiệu lực nguyên byte hoặc ánh xạ đầy đủ. Gỡ import, override hoặc fallback cũ đúng phần đã thay.
- Kiểm đúng đường nạp và khả năng tiếp quản; khép migration rồi tiếp task đã được giao trong cây.
- Người dùng không phải dò file/ID, xuất thêm gói về ChatGPT hoặc xác nhận lại cùng việc thay luật.

## 2. Xác định phạm vi theo task hiện có

Quyền của từng task lấy từ chỉ thị hiện hành của Owner được ghi trong task có sẵn. Ghi project/root, tập nguồn và điều khoản, phạm vi chỉ đọc/soạn/thử/chuyển/khôi phục, giới hạn và thời điểm. Tài liệu hoặc ZIP gửi để xem xét chỉ là dữ liệu. Hash xác nhận byte đang đối chiếu. Bằng chứng chấp thuận cần chỉ thị Owner và liên kết tới byte/phạm vi tương ứng. Dùng lại quyết định còn hiệu lực đúng phạm vi.

Gói 3.0.2 là nguồn HOST dùng chung. Ghi điều khoản địa phương nào giữ nguyên, điều khoản HOST nào được thay và nguồn kế nhiệm cụ thể. Quy tắc riêng dùng exact path/revision hoặc hash theo cổng đang có. Chuyển chính sách model theo R09 chỉ khi có quyền đổi định tuyến trong binding thực.

**Binding tối thiểu** điền ở task hoặc nguồn điều phối hiện có, trước khi đưa vào đường nạp. Dùng đường relative từ root nếu cùng repo. Với nhiều root/worktree, ghi đường đã resolve và phạm vi của từng root.

| Trường | Điều cần lưu |
|---|---|
| Dự án, root/worktree | Project ID, đường đã xác minh và client dùng từng root |
| Nguồn hiệu lực | AGENTS.md, cầu nối/import khi cần, luật và hợp đồng riêng, profile/hook ảnh hưởng, revision/hash theo dự án |
| Vận hành | Đường cây, task/checkpoint/nhật ký, chủ từng vùng và lifecycle hiện có, điểm chốt quyền/revision |
| Workflow | Nguồn thật cho từng trigger R18, skill đã bind hoặc vị trí mục 4–8 của workflow |
| Xuất và phục hồi | Hai đường dẫn cố định của cây/packet và nguồn snapshot theo R19. Preimage/custody, điều kiện phục hồi và nguồn quyết định Owner |

Ví dụ repo một root có thể trỏ tới `AGENTS.md`, `docs/QUY_TRINH_SKILL_VA_AGENT.md`, cây `docs/PROJECT_MAP.md` và issue đang giữ checkpoint, nếu đó là các nguồn thật. Đặt chỉ dẫn đọc binding ngắn ở nguồn được nạp. Giữ một đầu mối và sổ có sẵn. Dự án có registry riêng tiếp tục dùng registry đó.

Lệnh chỉ đọc/đánh giá/soạn/thử dùng vùng được cấp. Việc thay nguồn active, cập nhật currentness/reference, thay cấu hình client hoặc nghỉ hưu nguồn có cổng riêng theo đúng phạm vi Owner đã giao. Tool, ACL/sandbox, ngân sách, bảo vệ dữ liệu, sản phẩm, protected evaluation và các pause hiện hành giữ ranh giới riêng.

Giữ nguyên người đang giữ cây hoặc phạm vi dở cho đến bàn giao hợp lệ. Chưa xác minh liveness thì ghi đúng trạng thái. Gửi findings cho writer có quyền. Phần chuẩn bị độc lập vẫn tiếp tục trong phạm vi được giao.

## 3. Một task migration, một dấu vết phục hồi

Tìm task migration tương đương đã có trước khi tạo việc. Nếu cùng gói đã áp dụng và còn hợp lệ, chỉ kiểm delta cần thiết rồi tiếp việc, không thực hiện lại.

Trong task/nhật ký hiện có, giữ một bản ghi gồm:

- Dự án, quyết định Owner hiện tại, gói/phiên bản và identity HOST của người thực hiện.
- Nguồn luật/config được thay, preimage/hash, đích mới, nguồn backup và bước đã thực hiện.
- Task sản phẩm đang dở, checkpoint, claim, writer/job liên quan và accounting.
- Kết quả kiểm, lỗi còn lại, trạng thái activation/release và bước tiếp theo.

Đây là dữ liệu trong cơ chế sẵn có, không là registry hay state machine mới. Receipt/seal bất biến giữ nguyên; index append-only chỉ được bổ sung qua owner/helper hợp lệ.

## 4. Đọc nguồn thật một lần, không kiểm toán lại cả dự án

Agent tại máy tự xác định và đọc:

1. Toàn bộ cây hiện hành; đọc bù đoạn cắt hoặc dòng dài, không thay bằng grep/heading/hash.
2. Đồ thị luật thực có hiệu lực: global, parent, project, nested, imports, rules, profile, hook và cấu hình liên quan.
3. Core/quy tắc dự án đang thực sự được chọn và currentness/binding được dự án chỉ định.
4. Các hợp đồng hiện hành chịu tác động. Khi thay nguồn dẫn nhiều hợp đồng, xác định đủ nghĩa vụ và byte đang được dẫn. Nếu đã chuyển hợp lệ, kế thừa ánh xạ có chứng cứ, chỉ mở phần delta cần thiết.
5. README/schema/helper của lifecycle, claim, receipt, release, resume/transfer/recovery khi dự án sử dụng.
6. Nhật ký HOST, custody và trạng thái task/writer/job cần để bảo toàn việc dở.

Đọc đường dẫn và byte thực được nguồn dự án chọn. Nếu khác bản upload, xử lý theo nguồn thật, giữ pin có thẩm quyền.

Phạm vi này là đọc để thay hệ luật, không phải đọc lại toàn source, HISTORY hoặc dữ liệu chấm. Sau migration, chỉ nạp luật lõi và scope/skill có trigger.

## 5. Phân loại giữ nội dung, thay nguồn và nghỉ hưu

Lập bảng ngay trong task: nội dung cũ → giữ/chuyển/thay/nghỉ hưu → nguồn kế nhiệm → phần chịu tác động.

| Nhóm | Cách xử lý |
|---|---|
| Điều khoản ghim model trong HOST, luật riêng, binding và override cố định theo dự án | Thay đúng phạm vi bằng R09. Giữ lựa chọn B theo lần giao việc và xác minh yêu cầu, cấu hình, quan sát trên từng đường dùng |
| Kiến trúc, owner, ranh giới subsystem, dữ liệu và admission | Chuyển đầy đủ nội dung còn cần vào nguồn dự án kế nhiệm |
| Holdout/custody, tính trung lập, chất lượng và bằng chứng | Giữ bảo vệ; không biến migration thành miễn nghiệm thu sản phẩm |
| Thủ tục review được giao thay | Đối chiếu delta ở mục 7. Giữ các cổng hiện hành và phần nằm ngoài phạm vi |
| Task, quyết định, CAP/findings, checkpoint, receipt, accounting | Giữ dữ kiện và byte bất biến; cập nhật projection có căn cứ |
| Luật trùng, hết dùng hoặc bị thay | Loại khỏi đường nạp; lưu một bản phục hồi ngoài active |

Đích chung: `AGENTS.md` là luật tác nghiệp HOST, `CLAUDE.md` nhập cùng nguồn. Quy tắc riêng giữ nghĩa vụ sản phẩm với nguồn và phạm vi rõ. Nhật ký HOST ghi lựa chọn B và danh tính phiên. Canonical artifacts giữ mức trung lập được dự án yêu cầu.

Trước khi chuyển định tuyến, lập exact write set cho các điều khoản và override đang thật sự chi phối phạm vi đó. Đối chiếu nghĩa vụ và consumer đang phụ thuộc, thẩm quyền, writer, preimage/rollback, pin và đường nạp thực. Cắt các nguồn định tuyến cũ và nối R09 dưới cùng một lần chuyển đã được cấp quyền. Dừng phần phụ thuộc nếu chuỗi còn nạp hai lựa chọn cạnh tranh. Giữ các cổng dự án. Thay định tuyến HOST riêng không chuyển doctrine hay các quyền nghiệp vụ.

Agent tạo nội dung kế nhiệm sau khi đọc đủ nguồn địa phương. Có thể giữ cấu trúc core/scope hữu ích, nhưng phải chỉ rõ nguồn cũ đã hết hiệu lực và nguồn mới sở hữu từng nội dung. Dọn các import ẩn dẫn tới đúng nguồn đã được thay khi đạt điều kiện nghỉ hưu.

## 6. Chuẩn bị trước khi chuyển

1. Ghi identity khi nhận việc, kể cả chỉ đọc; worker thiếu quyền nhật ký gửi dữ kiện để coordinator ghi ngay.
2. Tách requested/configured/effective model/effort có nguồn; native ID thiếu thì `NOT_EXPOSED`, nhãn nội bộ không giả tên UI.
3. Chốt danh sách file/binding/helper cần đổi và phạm vi ghi; không mở thêm chức năng sản phẩm.
4. Giữ một bản byte-exact của nguồn sẽ thay trong custody hiện có, ngoài auto-discovery, theo quyền lưu trữ tương ứng.
5. Lưu checkpoint đủ staged/unstaged/untracked và tài sản ngoài Git cần thiết; giữ mục tiêu, phần dở, budget, attempts và jobs.
6. Soạn bản mới trong vùng chưa được tự nạp; đối chiếu ánh xạ nội dung và toàn bộ tham chiếu cần chuyển.
7. Chuẩn bị thao tác khôi phục chỉ cho tập thay đổi migration; không dùng reset/clean toàn repo.

Không xuất secrets/config riêng vào chat hoặc gói công khai. Backup byte-exact ở custody được phép khác với bản xuất đã che dữ liệu.

Các `SKILL.md` trong `.agents/skills/` gọi mục 4–8 của workflow đã bind. Link tương đối dùng khi mở repo luật trực tiếp. Khi cài vào dự án khác, dùng đường workflow trong binding dự án. Kiểm discovery, trigger đúng, trigger ngoài phạm vi và thao tác đọc nguồn thật trên client mục tiêu.

Native role profile chỉ được tái dùng/tạo sau khi kiểm schema client. Không đóng gói rồi chép một profile giả model/tool/quyền. Không đăng ký workflow HOST vào product Skill Registry để né admission.

## 7. Review delta và giữ cổng dự án

Nếu task giao thay thủ tục review, xác định đoạn cũ, nội dung mới, cổng và owner chịu trách nhiệm. Thực hiện review hiện hành với baseline, diff, bản đồ nghĩa vụ và chứng cứ, dùng reviewer khác tác giả khi cổng yêu cầu. Kiểm lại finding và phần chịu ảnh hưởng trong cùng ngân sách. Kiểm kê chỉ đọc ghi `review_count=0`.

Giữ cổng engineering, nghiệm thu sản phẩm, custody, quyền phát hành, điều kiện kế nhiệm, phục hồi và đọc lại trên phiên mới. Quy tắc review kế nhiệm có hiệu lực sau khi nguồn tương ứng được nghiệm thu và xác nhận active.

Kiểm kỹ thuật của tác giả, kết quả fixture, reviewer độc lập và kiểm tải từng client được ghi riêng. Sau sửa chỉ kiểm lại finding/tác động mới. Thiếu bằng chứng thiết yếu thì giữ checkpoint và ghi phần chưa đạt.

## 8. Chuyển active trong phạm vi một writer

1. Checkpoint và tạm dừng writer bị ảnh hưởng qua lifecycle thật; không dừng tất cả dự án hoặc tắt dịch vụ hợp lệ.
2. Đọc lại nguồn trước ghi; nếu có thay đổi ngoài dự kiến, hợp nhất delta thay vì ghi đè.
3. Đưa luật/skill HOST và quy tắc dự án kế nhiệm vào đúng vị trí.
4. Chuyển import, profile, hook, selector và binding; sửa helper đúng owner nếu cần thực thi lifecycle mới trong scope được giao.
5. Gỡ chỉ các đường nạp, override và fallback dẫn tới exact predecessor đã được giao thay. Điều kiện retirement và bảo toàn nghĩa vụ theo cổng dự án.
6. Cập nhật currentness/registry qua cơ chế thật, giữ receipt và index lịch sử bất biến.
7. Đọc lại file/binding, kiểm trạng thái và ghi bước đã hoàn tất vào task migration.

Nếu dự án dùng metadata currentness, kiểm các consumer thực sự sử dụng. Con trỏ, đường đọc trực tiếp và selector có thể độc lập. Chuyển đúng các đường trong write set đã được giao.

Không có transaction nhiều file thì dùng khoảng một writer và journal phục hồi từng bước; chưa cho tác động sản phẩm tiếp tục khi tập nguồn còn nửa cũ/nửa mới. Atomic replace một file không chứng minh toàn migration atomic.

Lưu từng bước và preimage của migration ngoài đường nạp. Writer kiểm project, scope, epoch/revision và quyền tại điểm ghi. Dùng helper và giao thức đã đăng ký của dự án cho claim, ghi log và nhả quyền nếu có. Adapter chỉ đọc chỉ chứng minh phép kiểm của nó. Dự án nhỏ dùng cơ chế một writer và task/checkpoint có sẵn.

Cập nhật helper/binding theo luật mới là thay đổi được review và kiểm; không tắt gate, sửa oracle hoặc mass-repin receipt để hợp thức hóa kết quả cũ.

## 9. Nghỉ hưu nguồn cũ, giữ lịch sử tìm được

- Nguồn cũ không còn được discovery/import/chọn làm authority/fallback.
- Giữ một bản byte-exact trong lịch sử/quarantine/custody không active, có liên kết nguồn kế nhiệm và hướng phục hồi.
- Không để `_old`, `backup` hoặc symlink vẫn nằm trong glob/chuỗi nạp.
- Receipt cũ giữ byte gốc. Nếu đường dẫn được chuyển, dùng relocation/custody mapping hợp lệ để tìm đúng byte lịch sử.
- Không sửa hash hàng loạt để gán PASS cũ cho luật/artifact mới; đánh giá applicability đúng phần chịu tác động.
- Chỉ xóa khỏi active sau khi nguồn kế nhiệm và đường phục hồi đã sẵn sàng; không xóa lịch sử/mã dưới nghĩa “bỏ luật cũ”.

Giữ nội dung kiến trúc trong luật mới không có nghĩa giữ nguồn luật cũ có hiệu lực. Cây vẫn là bản đồ dẫn tới chứng cứ, không tự trở thành doctrine hoặc receipt thay thế.

## 10. Kiểm có giới hạn và nạp đúng phiên

Sau chuyển active, thực hiện `LENH_CODEX_KIEM_TRA_SAU_THAY_LUAT.txt` trong cùng task hoặc mục hậu kiểm được liên kết, không tự tạo cuộc audit sản phẩm mới. Agent triển khai thực hiện các ca thuộc client/phạm vi mình có; Codex kiểm độc lập khi được giao. Nếu Codex cũng là bên vừa cài, cần reviewer khác người sửa kiểm delta liên quan, không tự gọi lần tự kiểm là độc lập. Tái dùng kết quả hậu kiểm còn đúng revision/phạm vi, không chạy trùng chỉ vì đổi tên lệnh. Lệnh này là tiêu chí của nhiệm vụ kiểm, không thêm nguồn luật active.

Dùng HK01–HK12 theo phần chịu ảnh hưởng để chốt đúng project/root và nested, client, nguồn cũ đã rút, B và danh tính, việc dở, lifecycle và cùng snapshot cây/packet. Ghi riêng kiểm staging và xác nhận trên phiên mới sau chuyển. Chưa chứng minh nguồn nạp, quyền hay hành vi thì giữ đúng tác động phụ thuộc. Không ghi thử vào cây thật, hạ gate hoặc sửa nghiệp vụ để làm hậu kiểm đạt.

Nếu turn/session còn giữ chỉ dẫn cũ, dùng reload hoặc phiên/process mới mà client thật hỗ trợ, nối vào checkpoint đã lưu. Không bịa lệnh/API reload hoặc coi sửa đĩa đã thay context đang chạy.

Host không tự mở/kiểm được cả hai client thì ghi rõ client nào đã kiểm, client nào CHƯA KIỂM và chuẩn bị bàn giao đủ nguồn. Không tuyên đạt cả hai. Có thể tiếp phần độc lập trên client đã kiểm; phần phụ thuộc client chưa kiểm phải giữ đúng trạng thái.

Kiểm lại chỉ phần bị sửa hoặc có rủi ro còn lại. Không biến lỗi cũ ngoài phạm vi thành một cuộc audit sản phẩm mới trước khi được kết thúc migration.

## 11. Ngắt giữa chừng, khôi phục và rollback

| Điểm ngắt | Hành động |
|---|---|
| Chưa đổi nguồn active | Giữ nguồn đang nhất quán; tiếp phần chuẩn bị từ bản ghi migration |
| Tập nguồn nửa cũ/nửa mới | Giữ tác động bị ảnh hưởng; hoàn tất bước còn lại hoặc rollback preimage của migration |
| Nguồn mới active nhưng loader sai | Sửa đúng binding/loader; rollback khi cần rồi kiểm lại tính nhất quán |
| Receipt xong, release chưa xong | Dùng recovery ở nhánh kết thúc mục 7 của workflow và helper có thẩm quyền; không rerun migration |
| Release xong, log/packet chưa cập nhật | Đọc registry/process thật rồi sửa projection; không suy từ log cũ |
| Task sản phẩm đã tiếp dưới luật mới | Checkpoint phần mới trước phục hồi; không rollback mù repo hoặc mất kết quả mới |
| Writer cũ quay lại | Kiểm quyền/decision tại điểm ghi/promote; không nhập kết quả muộn trái scope |

Đối chiếu bền từng bước sau ngắt với preimage và byte quan sát. Giữ tác động phụ thuộc khi còn nửa cũ/nửa mới. Nếu receipt hợp lệ đã ghi mà own ACTIVE còn, giữ cùng work-unit, không replay tác động, xác minh claim/receipt hiện tại và khép đúng release qua chủ có quyền. Nếu thiếu quyền hoặc thiếu proof thì lưu `CHỜ ĐỐI SOÁT`. Rollback đúng tập nguồn/binding cần phục hồi và giữ checkpoint mới sinh.

Không unlink claim ngoại lai vì cũ, sửa receipt bất biến hoặc replay tác động đã thành công. Rollback không phải hoàn thành migration; ghi đúng trạng thái và tiếp sửa trong quyền đã giao, không hỏi lại cùng chấp thuận.

## 12. Khép migration rồi tiếp việc

Khi đạt acceptance, chuyển sang nhánh kết thúc của cap-nhat-va-ban-giao ở mục 7 của workflow. Dùng R16/R22 và lifecycle dự án để chốt một lần. Nếu cần nhập delta sau nhả, giữ PENDING với đầu mối trong checkpoint.

Phân biệt kết quả chuyên môn, bàn giao/nhả quyền và job/tài nguyên còn sống. Dịch vụ cần tiếp tục phải có đầu mối vận hành thật; không tắt để báo “nhả sạch”.

Sau đó nhận lại task đã được giao trong cây/checkpoint bằng quyền hiện hành. Giữ work-unit/lineage; operation kế nhiệm chỉ khi lifecycle yêu cầu, có predecessor và không reset accounting.

Tiếp đúng công việc đã được giao trong giai đoạn hiện hành. Giữ phần có chứng cứ và phần đang có người giữ cho đến bàn giao hợp lệ.

Không dừng ở câu “đã cài luật, có muốn tiếp tục không?”. Nếu chỉ thiếu một quyết định sản phẩm mới thật sự cần, hoàn thành phần hợp lệ rồi hỏi đúng điểm đó với phương án cụ thể.

## 13. Báo cáo kết thúc ngắn, có thể kiểm

- Đã thay và nghỉ hưu nguồn nào; nguồn mới nào thực active; phần nào chỉ soạn/cài nhưng chưa kiểm.
- Byte lịch sử/checkpoint ở đâu, ánh xạ identity, receipt/release và tài nguyên còn sống.
- Những ca đã kiểm, giới hạn còn lại và ranh giới quyền/tool thực nếu bị chặn.
- Task nào đã tiếp tục, kết quả bước vừa làm và bước tiếp theo.

Không gửi thêm gói về ChatGPT làm điều kiện thi hành. Không tuyên toàn sản phẩm PASS từ việc thay luật. File này hoàn tất vai trò sau migration; vận hành thường ngày dùng luật và skill đã được nạp đúng.
